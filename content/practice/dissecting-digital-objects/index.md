---
title: "Dissecting Digital Objects"
subtitle: "Experiments in digital destruction"
category: digipres-lessons-learned
tags: ["Digital Preservation", "Keeping Codes", "Lessons Learned"]
layout: post
author: anj
shown: true
weight: 1
---

<!-- MarkdownTOC autolink="true" -->

- [Unsafe Device Removal](#unsafe-device-removal)
	- [Materials](#materials)
	- [Method](#method)
	- [Results](#results)
	- [Over to you](#over-to-you)
	- [Results](#results-1)

<!-- /MarkdownTOC -->

# Unsafe Device Removal #

Let's start with an experiment...

<!--break-->

## Materials ##

For this experiment, you will need:

1. An USB flash drive of little importance. One of those old sub-GB ones you got from that conference will do.
2. A copy of a digital file of great importance. Any format will do, as long as it's in a format you can open.


I'm going to use this drive:

![Test Drive]({{site.url}}/digipres-lessons-learned/images/save-as/save-as-test-drive.jpg)

...and this JPEG:

![My father and my son, alike.]({{site.baseurl}}/digipres-lessons-learned/images/save-as/best-test-image.jpg)

## Method ##

1. Copy the test file to the USB flash drive. *Do not use your only copy of the precious file!*
2. Open up the test file from the USB drive, as you usually would (i.e. using the usual app for that format).
3. Pull out the USB flash drive. *Do Not Eject It Properly!* **Just yank it right out!**[^1]
    * **Optional:** [Throw the USB drive into a blender and destroy it utterly](https://www.youtube.com/watch?v=y2eNhPC8wCQ).
4. Observe what happens.


## Results ##

In my experiment, the first thing that happened was...

![Disk Not Ejected Properly]({{site.url}}/digipres-lessons-learned/images/save-as/save-as-oops.jpg)

...but beside this admonishment, the image was still there...

![But Still There]({{site.url}}/digipres-lessons-learned/images/save-as/save-as-still-there.jpg)

The bitstream was gone (optionally blended into oblivion -- the Digital Object destroyed). But the image was still on the screen. I bet yours is still there too.

But right now, it's at risk. All it takes is loss of power to this machine, and the file will blink out of existence.[^2]

Can you press 'Save as...', and get a new bitstream back? It depends on the software. 

When I [tried this with Apple Preview](https://www.flickr.com/photos/anjacks0n/sets/72157655724233440), I couldn't save the image, even though I could see it. 

![Apple Preview Says No]({{site.url}}/digipres-lessons-learned/images/save-as/save-as-preview-says-no.png)

The only way to save it seemed to be as a desktop screenshot, which I would then need to crop to get back an acceptable image.

But re-running the same experiment with image editing software (specifically the [GIMP](http://www.gimp.org/)), I could press 'Save as...' and a new bitstream was written. Not *exactly* the same as the original, but good enough.[^3]


## Over to you ##

I'd be fascinated to know what happens on other platforms and with other software, so please get in touch if you've tried this. I'd also be curious to know how the choice of format affects the outcome. If anyone has any results to share, I'll collect them together in a follow-up post.


## Results

Following my [proposed experiment in data destruction](/2017/04/10/unsafe-device-removal/), a few kind readers tried it out and let me know what happened[^4]. I've summarised the results below, to try and see if there's any common pattern.

<!--break-->

| Software | Format | Was recovery possible? |
| ---------|--------|------------------------|
| Apple Preview | JPEG | No (rendered image still shown and could be captured via screenshot)[^5] |
| GIMP | JPEG | Yes (with minor alterations to the data, likely [within allowed limits for JPEG][1i])[^5] |
| Imagemagick display | JPEG | Yes (result not binary-identical)[^6] |
| Ubuntu Image Viewer | JPEG | No[^7] |
| Ubuntu Document Viewer | PDF | Yes[^7] |
| PDF reader | PDF | PDF from a browser, stay in a PDF reader after the browser closes but can't be saved[^8] |
| Word (Windows 95) | DOC (on a floppy!) | No (but re-inserting the floppy worked!)[^9] |

As far as I can tell from this data, there isn't much of a pattern here. Broadly, the observed behaviour seems to depend on the software rather than the format, and 'viewer' style applications appear less likely to allow re-saving than 'editor' apps (but the behaviour of the Ubuntu Document Viewer shows this is not a robust finding). All we can be sure of at this point is this: "It's complicated".

To find out what's going on, we'll need to look more closely at what happens when we open a file...

----

[^1]: Go on, admit it, you've always wanted to try this and see what happens. Well, now you get to do it. For Science.
[^2]: And entropy will win. And we don't want *that*.
[^3]: The two images were highly similar, with a [PSNR](https://en.wikipedia.org/wiki/Peak_signal-to-noise_ratio) of just over 56dB and with a distribution of differences that looks like [this]({{site.url}}/digipres-lessons-learned/images/save-as/difference.png). It is not clear if the variation is due to small differences in JPEG compression parameters, or if all the parameters are the same but the implementations have small difference in execution (e.g. rounding errors).
[^4]: Thanks also to [Nick Krabbenhöft][2i] for [pointing out][3i] that I could have been a bit more careful about my original experiment, and that would have helped work out where the JPEG differences came from in the case of re-saving the image from GIMP.  That said, I expect such minor differences are down to small variations in the implementation of the JPEG decompression scheme, [as permitted by the standard][1i]. i.e. my final image is likely the no *more* different that the *same original image* might be when rendered by a *different software application*.
[^5]: See [the original post](/2017/04/10/unsafe-device-removal/)
[^6]: Result from [@atomotic](http://anjackson.net/2017/04/10/unsafe-device-removal/#comment-3249487142)
[^7]: Result from [@archivalistic](https://twitter.com/archivalistic/status/851907815673286656)
[^8]: From [@andrewjbtw](https://twitter.com/andrewjbtw/status/851530416590790656)
[^9]: Also from [@andrewjbtw](https://twitter.com/andrewjbtw/status/851531680632365056)

[1i]: https://photo.stackexchange.com/a/83892/62442
[2i]: https://twitter.com/nkrabben
[3i]: /2017/04/10/unsafe-device-removal/#comment-3249002689