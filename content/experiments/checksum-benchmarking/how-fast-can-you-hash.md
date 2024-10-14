---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.16.4
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

How Fast Can You Hash
--------------------

This notebook runs some basic performance tests to determine how fast we can run data through the SHA-512 or MD5 algorithms.

This test uses fairly large files in an attempt to minimise the effect of the operating system caching disk data in RAM.

First we set up some functions that perform basic operations to compare:

* `zero_to_null` just passes zeros through the CPU, and so is as fast as anything could possibly go.
* `zero_to_hash` runs the zeros through SHA512, so is the fastest we can possibly hash (no disk I/O).
* `zero_to_file` streams the zeros to a file - disk write I/O only, no hash.
* `file_to_hash` hashes a file (created with `file_to_zero`), so this is disk read I/O and hashing.

```{code-cell} ipython3
---
jupyter:
  outputs_hidden: false
---
from generate import ZERO_TO_NULL, cmd_runner

# And as an example, here's how we can run them:
print(cmd_runner(ZERO_TO_NULL, None).strip().decode())
```

Now we can run them in parallel..., and ramp them up to see what happens when we run eight at once...

+++

Ramping zero-to-null tops out at 4 parallel processes, which make sense because this laptop has four cores.

```{code-cell} ipython3
---
jupyter:
  outputs_hidden: false
---
import pandas as pd
import altair as alt
from altair import datum

# Load the data
df = pd.DataFrame(pd.read_json('hasher-runs-Framework-13-2.jsonl', lines=True))

# Lay out the useful results:
alt.Chart(df).mark_line(point=True).encode(
    x='n_proc:O',
    y='MBps:Q',
    color='hash:N',
    tooltip=['mode', 'n_files', 'n_proc', 'hash', 'MBps' ],
).transform_filter(
    # Filters out the results where both hash and mode are empty:
    (datum.hash != '' ) | ( datum.mode != '')
).properties(
    width=400,
    height=150,
).facet(
    row='mode:N'
)
```

Similarly ramping the hash function (no I/O) tops out at 4 cores, at about 950MB/s (about 300MB/s/core but it seems there are some overheads/contention that drops it down slightly when running on all four).

+++ {"jupyter": {"outputs_hidden": true}}

Switching to MD5, the maximum speed is about 2800MB/s (interesting that the performance now tops out at 6, which implies some level of low-level paralellism is allowing this to run even faster!)

+++

Remarkably, on this laptop, we can stream data into a file at 1,200MB/s (!) which is shared across all cores. Further testing outside of this notebook indicated that this was real I/O speed and not due to files being cached in RAM.

+++

Consequently, as the I/O is so fast, and the CPU has only four cores, we cannot saturate the bandwith of this machine:

+++

So, in general, if we're hashing lots of files, we'll tend to run out of I/O before we run out of CPU. However, it depends on lots of things, so it's probably worth benchmarking your own kit.

Note that, if the data you are caching is fairly small, your operating system will likely cache it all in RAM rather ran re-reading from disk. In that case you'll get much higher speeds when tests are re-run.

Also, there's some subtle issues not investigated here. For example, if you have a lot of small files, then your read speeds can be very low on HDD-based systems, because the disk spends more time seeking to the start of files than it does reading data, and seeking is generally slower than reading.

Secondly, on some systems, particularly smaller HDD arrays, I/O speed can drop when you run multiple threads, because the different read requests start to compete with each-other. More heavily RAID-ed systems can compensate for this, but you only have so make HD read heads you can position at one time, and the precise balance will depend on file sizes and how they are distributed across the drives.

Generally, with SSD's, these issues are less severe.

```{code-cell} ipython3
---
jupyter:
  outputs_hidden: true
---

```
