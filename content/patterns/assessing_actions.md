# Assessing Actions

When preserving digital content, after keeping the bitstreams safe and making sure people can find them, the next problem is knowing that the content they access is working as it should. Are the items, as presented by the archive, accurate representations of what the archive originally received? And can we prove this to be the case?

Maintaining this fidelity is particularly difficult when steps have been taken to mitigate access problems due to format obsolescence, e.g. format conversion, or presentation via emulated environments (a.k.a. _preservation actions_).

How can we verify we haven't lost anything important? Where we have intervened, how can we be sure we've done the job right? Well, we can start by checking our own results.

TODO Link to regression testing...


## Reversibility

When converting files from one format to another, it is sometimes possible to verify no information has been lost by reversing the transformation, and verifying that the original files can be recovered exactly.

For example, this is one way to verify that collections of files have been repackaged correctly.  If, for example, your archive received a set of files for ingest, and the ingested form uses some kind of packaging (e.g. ZIP or TAR or Bag-It), then it should be possible to re-generate the original submission and so verify nothing was missed. 

However, in general, it is difficult to ensure the original is regenerated _exactly as it was_ because of the variations in encoding that most formats permit.  For example, if you imagine transforming the data in some XML file from one XML schema to another, then _precisely_ reversing that conversion will be highly dependent on how tabs, spaces and newlines are handled, as well as the ordering and structure of the elements themselves. Depending on the schema, equivalent documents may allow very different encodings.[^1]

[^1]: In some cases, it may be possible to verify that a format conversion retains the same information even if the encoding shifts (see [Understanding Tools & Formats Via Bitwise Analysis](http://anjackson.github.io/keeping-codes/experiments/understanding-tools-and-formats-via-bitwise-analysis.html)), but this remains an unresolved problem at present.

While in an ideal world all interventions would be reversible, there are many cases where some information loss is unavoidable.  Even where it is possible, re-generating the originals is also quite expensive in terms of the computational resources required.

Finally, the ability to reverse a format conversion does not by itself ensure that the item will be uncorrupted when accessed. The same information may be present, but if the new format and it's access software do not interpret the information in the same way, then the information is as good as lost.

### Examples

There seem to be very few examples of reversible transformations being used in practice. _Please get in touch if you are aware of any!_

#### Patching Buggy Binaries at The National Archives

As part of a digitisation project at the UK's National Archives, an unfortunate bug in the JPEG2000 software they were using created some minor errors in their image files while updating the embedded metadata.

A small program was created to fix the files, but on it's own, this broke the chain of authenticity back to the checksum supplied with the original files. To resolve this, they compared the fixed and original JP2 files and stored a patch file that records the difference between the two files. This patch file can be combined with the repaired file to precisely reverse the repair, at which point the checksum chain can be verified.

* [Tweet by @DavidUnderdown9](https://twitter.com/DavidUnderdown9/status/1478131136278708224)

## Significant Properties

The idea of "Significant Properties" (a.k.a. "Significant Characteristics", or "Transformation Information Properties" in OAIS) has a long and complex history in the research and practice of digital preservation. The earliest definition I'm aware of dates from 2002:

> "The Cedars Project has coined the term “significant properties” to describe those components of a digital object deemed necessary for its long-term preservation."
> 
> [Cedars Guide to Digital Collection Management, The Cedars Project, 2002, §4.31, p. 15](https://www.webarchive.org.uk/wayback/archive/20050410120000/http://www.leeds.ac.uk/cedars/guideto/collmanagement/guidetocolman.pdf)

Later definitions tend to go into a bit more detail, but the core idea remains the same. For example: 

> "Significant properties: the characteristics of digital objects that must be preserved over time in order to ensure the continued accessibility, usability, and meaning of the objects, and their capacity to be accepted as evidence of what they purport to record."
> 
> [Significant Properties of Digital Objects, Andrew Wilson, National Archives of Australia, 2008, p. 15](https://www.dpconline.org/docs/miscellaneous/events/142-presentation-wilson/file)

If course, in natural conversation, one could hardly disagree with the assertion that we should aim to _preserve the significant properties of our digital content_. As a general statement of intent, this is all good. But this framing encourages a literal interpretation that pushed us along an overly prescriptive path.

Because, if the goal of preservation is to preserve the significant properties of digital objects, then surely the job of digital preservation it to determine what those properties are for each object, and check them whenever we need to check we've not lost anything?

And this needs to be automated, so we need tools that will extract all the Properties from our digital objects and record them as metadata. We decide which of those Properties we think are Significant, and we'll keep them, and we'll check them, and that way we know we've got what we need.

This sounds reasonable, at least _in theory_.[^2] The problem is that, assuming it can be made to work at all, it still represents an absolutely _huge_ amount of effort, far beyond the grasp of the digital preservation community.

[^2]: However, it is not certain that this is even theoretically possible, as this approach requires the underlying data model being used to describe the properties to be remarkably universal. It has to losslessly capture the details of, say, any image format, both now and in the future. And do so in a way that can cover all the different subjective judgments of significance that are encountered over that time. _??? Limit this here and go deeper elsewhere?_

### Significant Properties Type 1: Technical Metadata

It all starts simply enough.  Take, for example, this list of "Significant characteristics of audio files" copied from [the Archivematica wiki](https://wiki.archivematica.org/Significant_characteristics_of_audio_files).

| **property value** | **component** | **notes**|
|--------------------|---------------|----------- |
| duration           | content       |            |
| number of channels | content       | May be expressed as a number or as a description such as "mono", "stereo" or "surround" etc. |
| channel mapping    | structure     | For example, in stereo files, a channel number will be linked to either the left or the right ("channelNum="0" mapLocation="LEFT"/channelNum="1" mapLocation="RIGHT")  |
| sampling frequency | rendering     | This property may not be preserved through transformation to a preservation format, since conversion to WAV entails the use of a sampling frequency that is used by the WAV format (eg 441000 HZ, 48000 HZ, 96000 HZ). However, the sampling frequency of the preservation format should not be lower than that of the original format. |
| bit depth          | rendering     | The bit depth of the preservation format will be 16 bits unless the bit depth of the original format is higher (e.g. 24 bits). |

While these properties may be of interest, it is important to note that _none_ of these actually describe the _content_ we are trying to preserve. If we validate a format conversion based on these properties, an output that was _entirely silent_ would pass every test and go unnoticed. Conversely, most of these could be changed (e.g. a little silence at the end, a doubled sampling frequency or bit depth, etc.) while leaving the actual content wholly intact. Therefore, these types of properties _cannot_ be said to be _Significant Properties_ at all, because they do not describe the content to be preserved. This doesn't mean they are not useful, just that they serve a different purpose (as we'll cover in a later section).

### Significant Properties Type 2: Feature Checklists


```{figure} ./images/sp_features.png
---
width: 70%
name: sp-features
---
InSPECT Project Final Report
```


### Significant Properties Type 3: Describing Content


To act as Significant Properties, we need to find a way to describe the audio signal itself, but that is _exactly what an audio format does_. In other words, creating any Significant Properties scheme that is sophisticated enough to describe the actual content of a file will be like creating a dedicated 'archival format', which is just like a real data format, except we alone are responsible for every aspect of format development, support and maintenance.

And that's just thinking about audio files.  The logical end-point of the Significant Properties paradigm is that we must be able to describe _all_ the aspects of _every_ digital object, for _every_ format we have. This description needs to be complete enough to act as a 'super-format' that can capture all know formats in a unified and universal data model, and capable of describing both the data encoding and how it should be interpreted.

But the format specifications that exist are not expressed in the kind of machine-readable form that would facilitate this, and many of the details are buried in the implementations of those formats, where they may not even be interpreted consistently.

Therefore, a necessary (but not sufficient) condition for Significant Properties to work as originally hoped is for the digital preservation community to understand, document and automate the interpretation of _all_ features of _all_ digital formats and to do it _better_ than the entire IT industry has managed thus far.

This is not a reasonable expectation to place upon ourselves.

Realistically, the organizations that are tasked with preserving digital culture can only hope to understand a handful of formats that deeply. And rather than inventing our own, it makes more sense to track and adopt suitable formats from the wider Information Technology industry. Especially where we can choose formats that have become widely supported and inter-operable standards, even if this means relaxing our requirements.

### Examples

#### XCL - eXtensible Characterization Language

If the extrapolation of Significant Properties outlined above sounds like an unrealistic straw-man argument, then you probably never heard about the [XCL project](http://web.archive.org/web/20160104015336/http://planetarium.hki.uni-koeln.de/planets_cms/node/1.html). This research project was a major components of the [PLANETS Project](https://planets-project.eu/), which was my route into the field of digital preservation.

The project revolved around two XML schemas. The Extensible Characterisation Definition Language (XCDL) and the Extensible Characterisation Extraction Language (XCEL), which describe formats and the information contained within individual files respectively.

The idea was that any group of formats of a given _kind_ (e.g. images, audio, video, texts) could be described by a single XCDL document, which would fully describe all the potentially-significant properties of that kind of file, including the content itself (e.g. pixel channels and values for images, sentences and paragraphs for texts).  One digital item expressed in this XML format could then be compared with another of the same _kind_, because both are covered by the same data model no matter what the original format.

The task of turning an original file into it's XCDL representation was performed by XCEL. This provided a way to describe binary formats in XML, and defined how to break up and read the raw bytes to transform them into the XCDL representation. The idea was that XCEL and XCDL could be combined to allow things like format migration to be precisely evaluated.[^3]

[^3]: See [here](https://planets-project.eu/docs/presentations/Planets_Tools-and-Trends_ManfredThaller.pdf) and [here](https://planets-project.eu/docs/presentations/manfred_thaller.pdf) for more details about characterization and XCL.

```{figure} ./images/sp_xcl.jpg
---
width: 70%
name: sp-xcl
---
The vision for XCL
```

After many years of funding, with multiple Ph.D. students working on it, XCL covered a modest subset of the functionality of a handful of file formats.  It was most successful with image formats, but these are relatively simple, and not at much risk of become obsolete. Even there, it was unclear that things like embedded metadata and the subtleties of transformations between colour spaces were being handled adequately. Perhaps it should not have been a suprise to find that writing complex software like a format parser in an XML-based language turned out to be very hard work indeed.

At the time, I found this work fascinating and compelling, but in retrospect I've come to regard it as a failed experiment, but an important one, because it showed the limits of Significant Properties paradigm.

The limits of this approach were further underlined by another PLANETS project output, ["Significance Is in the Eye of the Stakeholder"](https://planets-project.eu/docs/papers/Dappert_SignificantCharacteristics_ECDL2009.pdf). This showed that _significance_ was much more complex than picking which properties survived, not just at a technical level, but also because significance is subjective and variable across time and between different stakeholder communities.

Like Wile E. Coyote running off a cliff edge, it took a while, but in time these two pieces of work led me to conclude that the Significant Properties approach is, at best, utterly impractical.


#### Nation Archives Australia



#### Spreadsheet work




## Canary Properties

hashes

## Differences

diff.

SVG GitHub diff.


## Performance Comparison

When we convert an objects format, or change the way we present the item to our patrons, the most basic thing we can do to verify if it's working is to check it ourselves first. This isn't as easy as it sounds, as it can be hard to ensure the evaluation process is consistent across individuals and over time, but it's an important part of any preservation strategy.

However, the bigger problem is that it requires a large amount of effort to manually inspect items, and most organizations have far more content than they can possibly expect to inspect.  In short, manual inspection doesn't scale.

Randomized spot-checks remain critical, and collaborative efforts like crowd-sourcing can go a long way. But to be _sure_ we haven't lost anything, we need to automate the process.

### Web Archiving Quality Assurance

It is common practice to manually inspect the content that has been captured by a web archive crawl.  The process of gathering web content in complex, and it's easy to accidentally miss resources that are required for the pages to be complete.  Similarly, the process of making archived content accessible is also complex, and there are many sites that are difficult or even impossible to 'playback' accurately.

This process of inspection is difficult work, and it often requires a very good understanding of web technologies in order to be able to work out what's gone wrong. For example, only a handful of staff members are able to perform this work at the UK Web Archive, so while we check what we can, we have only been able to check tens of thousands of pages from the millions of sites we have gathered over the years. This is why many web archives are starting to explore how automation can be used to augment or replace manual quality assurance processes.

_**TODO:** Merge these into the text? Or have small link sections for every example throughout?_
_**TODO:** Discuss automation vs manual.

 * [How good is good enough? – Quality Assurance of harvested web resources (2012)](https://blogs.bl.uk/webarchive/2012/10/how-good-is-good-enough-quality-assurance-of-harvested-web-resources.html)
 * [Quality Assurance Paradigms in Web Archiving Pre and Post Legal Deposit (2014)](https://journals.sagepub.com/doi/abs/10.7227/ALX.0020?journalCode=alaa)
 * [Current Quality Assurance Practices in Web Archiving (2014)](https://digital.library.unt.edu/ark:/67531/metadc333026/)
 * [Why and how do we Quality Assure (QA) websites at the BLWA? (2017)](https://blogs.bodleian.ox.ac.uk/archivesandmanuscripts/2017/10/10/why-and-how-do-we-quality-assure-qa-websites-at-the-blwa/)
 * [How to automate web archiving quality assurance without a programmer (2018)](https://blog.nationalarchives.gov.uk/automate-web-archiving-quality-assurance-without-programmer/)



## Indirect Comparison

e.g. generate plain text version of 

That said, as we will discuss below, this kind of validation is often better handled via other means, like validating checksum manifests.


## Difference Properties

PSNR etc.

#### TIFF to JP2 Validation

PSNR
