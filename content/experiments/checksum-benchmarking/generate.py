#!/usr/bin/env python3

import multiprocessing as mp
from functools import partial
import subprocess
import logging
import json
import time
import re

logger = logging.getLogger(__name__)

BYTES_MATCHER = re.compile("^(\d+) bytes ", re.MULTILINE)


ZERO_TO_NULL = "dd if=/dev/zero of=/dev/null bs=1000k count=1000"
ZERO_TO_HASH = "dd if=/dev/zero bs=1000k count=1000 | openssl dgst -sha512"
ZERO_TO_HASH_MD5 = "dd if=/dev/zero bs=1000k count=1000 | openssl dgst -md5"
ZERO_TO_FILES = "dd if=/dev/zero of=test.zero.%(suffix)s bs=1000k count=1000"
# Now use the files set up by ZERO_TO_FILES
FILES_TO_NULL = "dd if=test.zero.%(suffix)s of=/dev/null bs=1000k count=1000"
FILES_TO_HASH = "dd if=test.zero.%(suffix)s bs=1000k count=1000 | openssl dgst -sha512"
FILES_TO_HASH_MD5 = "dd if=test.zero.%(suffix)s bs=1000k count=1000 | openssl dgst -md5"

# Define a suitable function for running in parallel:
def cmd_runner(template, x):
    command = template % { 'suffix': x }
    return subprocess.check_output(command, stderr=subprocess.STDOUT,shell=True)
    
# Now another function that will ramp up the pool size, defaulting to 2 times number of CPUs available:
# 'mode' should be 'r' or 'w' when dealing with files
def ramp(cmd_template, hash_name='', mode='', max_pool=2*mp.cpu_count()):
    logger.warning('Running ramp for "%s"...' % cmd_template)
    # start worker processes
    for size in range(1, max_pool + 1):
        #logger.warning(f'Starting with {size}...')
        with mp.Pool(processes=size) as pool:
            start = time.time()
            # Set up file count:
            if mode:
                n_files = size
            else:
                n_files = 0
            # Set up counters
            total_bytes = 0
            total_bytes_per_sec = 0
            # Run the same repeated template for each process in the pool:
            for i in pool.imap_unordered(partial(cmd_runner, cmd_template), range(size)):
                total_bytes += int(BYTES_MATCHER.search(i.decode("utf-8")).group(1))
            # Record the end time:
            end = time.time()
            duration = end - start
            yield {
                'hash': hash_name,
                'mode': mode,
                'n_files': n_files,
                'n_proc': size, 
                'total_bytes': total_bytes,
                'time_s': duration,
                'bps': total_bytes/duration,
                'MBps': (total_bytes/duration)/1000000
            }

def write_out_json(f, source):
    for r in source:
        f.write(json.dumps(r))
        f.write('\n')

if __name__ == '__main__':
    with open('hasher-runs.jsonl', 'w') as f:
        # CPU-only:
        write_out_json(f, ramp(ZERO_TO_NULL))
        write_out_json(f, ramp(ZERO_TO_HASH, hash_name='SHA512'))
        write_out_json(f, ramp(ZERO_TO_HASH_MD5, hash_name='MD5'))
        # Now write files:
        write_out_json(f, ramp(ZERO_TO_FILES, mode='w'))
        # Now read those files:
        write_out_json(f, ramp(FILES_TO_NULL, mode='r'))
        write_out_json(f, ramp(FILES_TO_HASH, mode='r', hash_name='SHA512'))
        write_out_json(f, ramp(FILES_TO_HASH_MD5, mode='r', hash_name='MD5'))
