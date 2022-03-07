# Information Flow

The [Open Archival Information System (OAIS)](https://en.wikipedia.org/wiki/Open_Archival_Information_System) reference model is generally very high-level. There are a _lot_ of different ways of running an archive that would still fit. 

But one thing it is very clear about is the overall flow of information through the archive. 

## Flow 1: The Line

```{glue:figure} oais_environment_dot
:figwidth: 100%
:name: "oais_environment_dot"

```

> OAIS §1.4 - CONFORMANCE:
> "A conforming OAIS Archive implementation shall support the model of information 
described in 2.2"
>
> OAIS §2.2.3 - INFORMATION PACKAGE VARIANTS:
> "Within the OAIS one or more SIPs are transformed into one or more Archival Information Packages  (AIPs)  for  preservation. [...] In response to a request, the OAIS provides all or a part of an AIP to a Consumer in the form of a Dissemination Information Package (DIP). "

Under OAIS, Submission Information Packages (SIPs) come in from Producers, are managed as Archival Information Packages (AIPs), and these AIPs are then used to generate the Dissemination Information Packages (DIPs) that serve the needs of the archive's user community a.k.a. Consumers. This fundemental design pattern for digital archives -- this way of describing the overall flow of archival information -- can be visualised via this simple diagram:


```{glue:figure} flow_line_dot
:figwidth: 100%
:name: "flow_line_dot"

```

This linear flow of information is one of the strengths of the OAIS model, because by generating the DIP from the AIP, we ensure that all the information we might need to (re)create a new DIP is in the Archival Store.

For an implementation to follow this pattern, it must ensure that _only_ information that is in the AIP was used in the creation of the DIP, and there is no dependency on the SIP. OAIS does this by specifying that the DIP is generated from the AIP held on Archival Storage, after the SIP has been discarded. This could be immediately after ingest, or some time later, or on demand -- the important thing is that it's post-ingest.

Here are some examples of digital preservation systems that enforce the OAIS information flow by generating access versions after ingest has been completed, thus referring only to the archived content.

### The UK Web Archive

Like most public web archives, the [UK Web Archive](https://www.webarchive.org.uk/) generates access copies on demand. The archived web resources are captured in [WARC](https://en.wikipedia.org/wiki/Web_ARChive) files, which are placed on archival storage before the necessary indexes are generated from them in order to enable access. When individual items are requested, the relevant records are copied from the AIP and the access version (DIP) is generated from the archival version during playback (dynamic requests and responses are indicated by arrows going on both directions).[^3]


```{glue:figure} flow_line_warc_dot
:figwidth: 100%
:name: "flow_line_warc_dot"

```


### The Internet Archive

The [Internet Archive](https://archive.org)'s web archive also generates access versions on demand.  For their other types of content, the documentation makes it clear that their archival system generates various derivatives for items after they have been ingested/uploaded. See for example this [documentation on type of derivatives they generate](https://help.archive.org/hc/en-us/articles/360014487651-Files-Formats-and-Derivatives-A-Basic-Guide), and this [summary table showing all the format conversions they do](https://archive.org/help/derivatives.php). 


## Flow 2: The Stop

The linear workflow described above may seem obvious, perhaps even inevitable, but it's not. It's not that unusual to find archives where there is _no flow at all_.  This corresponds to so called "dark archives" - ones that cannot be accessed except by the people who manage the archive. Usually, this is because the content is available elsewhere, and the archive is acting as a 'backup copy' in case the original goes away.

```{glue:figure} flow_stop_dot
:figwidth: 100%
:name: "flow_stop_dot"

```

In these cases, the focus tends to be on ingesting the content, and not on how that content might be used in the future. There may be DIPs, but they are not well tested because no-one really uses them much. Or there may be no DIPs at all, or just some theoretical DIP based on an imagined future.

The danger here is that it's possible to miss some information you need from the SIP, or from the wider context, because you'd only realise you needed it when your user community started trying to access the material. Ideally, to mitigate aganist this risk, it is necessary to either encourage real usage, or at least simulate it, so that access problems can be identified while there is still some hope of resolving them. Otherwise, your AIPs are like a backup that's never been tested.

In practice, access is rarely supported or simulated. Instead, to avoid losing data, the whole SIP is kept and embedded within the AIP as-is.  This still assumes there has been no problem in the creation and transfer of the SIP itself, relying on ingest-time validation to pick up any problems at an early stage.


### The UK Web Archive

While the UK Web Archive has thousands of open-access websites, we also archive many millions of sites under Non-Print Legal Deposit terms. This places heavy restrictions on access to those site, so in practice it is very unlikely that many of those sites will be viewed frequently enough to pick up any issues while we can still resolve them. To mitigate this issue, we rely largely on manual quality assurance, but of course this is not something we can scale across the whole collection.

We are currently working towards automating some of the QA processes. For example, for many years we have been collecting screenshots of how the original websites looked when the web crawler originally visited them. The next step will be to add a post-ingest process that takes a screenshot of the archived web page in the same way as the crawler, allowing the images to be directly compared. This should highlight any issues and focus our efforts on where the archive needs to be improved.

We have also been working towards publishing non-consuptive datasets based on our holdings. These are no substitute for the original web pages, but surrogates are rich enough that meaningful research can be done with them, and this can help identify gaps in our collection.

### Electronic Journals

Due to their combined importance and cost, eJournals are often 'backed up' in dark archives like CLOCKSS or Portico. Usually, access to eJournals is via the publisher sites, and the archived copies only become active if the publisher shuts down.  Here, AIPs usually contain all the SIP information, and the overall structure and content has to be clearly defined and validated. The handling of additional content ....



## Flow 3: The Fork

The final class of information flow breaks the linear model entirely: while there is always a line from ingest to access[^1], there is sometimes a fork in the road.

```{glue:figure} flow_fork_dot
:figwidth: 100%
:name: "flow_fork_dot"

```

In this kind of split workflow, both the AIP and the DIP are generated directly from the SIP. In contrast to the linear flow described above, this design pattern _does not automatically ensure_ that the AIP contains all the information we need to generate the DIP. This is not to say that this risk cannot be addressed, rather the point is that the implementation has to do _additional work_ to make sure that this is the case.

One of the reasons why this can happen is that, during the design and implementation of archival workflows, it is common to try and perform a lot of processing up-front. Schematically, the result can look something like this:

```{glue:figure} flow_fork_dip_ingest_dot
:figwidth: 100%
:name: "flow_fork_dip_ingest_dot"

```

Here I am using _Ingest_, _Store_ and _Access_ to identify processing contexts, covering all the functions associated with that phase of the workflow. In this example, during the _Ingest_ phase, the incoming packages have been used to generate the DIP prior to the finalisation of the AIP. Only after both have been created are they transferred to the appropriate storage.  This means it is _possible_ for the AIP and DIP to diverge.

In many cases, especially those where the critical payload of each package is a single file, this is a modest burden, because when the number of files involved is small, it's easier to keep track of individual files, their checksums, and their relationships. As things get more complex, it becomes easier for mistakes to be made.

Additionally, ensuring the AIP and DIP are stored together in a single coherent transaction also requires some care, in order to ensure that the stored items remain consistent through network and system outages.[^2]

These potential risks are certainly manageable - the point is simply that these risks arise because of the decision to perform more processing up front.  This does not mean "The Fork" is a _bad_ pattern to follow. Indeed, in those cases where we can confidently verify the completeness of DIPs, generating them early helps identify problems as soon as possible. But we should be aware of the consequences of choosing this workflow pattern and make sure the benefits of up-front processing are worth the costs.


### An Outsourced Digitization

One real example involved a digitization project where much of the work had been outsourced to a third-party. The decision had been made to get the external partner to generate "access copies" as well as the long-term "preservation copies".

The preservation version consisted of high-resolution, full page TIFF files and associated metadata tying each set of TIFFs together, mapping back to the original publication. However, the access versions were not simply JPEGs of the preservation versions, but were also broken up at the level of individual articles. This worked well for access purposes at the time of the project.

The problem was the segmentation process had not been properly documented. The coordinates on the TIFF version that corresponded to the positions of the JPEG versions had been lost. This meant that when the access system became obsolete, it was not be possible to replace it like-for-like, i.e. while still preserving the same article-level experience. 

### Normalization on Ingest

Many archives operate under a policy of normalising content at ingest time, often under the guise of supporting "preservation copies" and "access copies".  Here, [Archivematica]() provides a useful example, as it is a widely used digital preservation system that provides facilities for normalisation of both AIP and DIP. Reading [the documentation]() it is clear that Archivematica _usually_ performs all processing up front, prior to ingest: the DIP is clearly generated directly from the SIP, but the system takes steps to ensure nothing is lost by making the original SIP forms the basis of the AIP. Archivematica does make it possible to derive access copies in a post-ingest process as part of the 're-ingest' workflow, but this is not the normal mode of operation, and calling it 're-ingest' seems likely to discourage its use.

While some of this is specific to Archivematica, the fact is the documentation for other digital preservation systems and services is often not open or detailed enough to make it clear exactly what is going on. But any system that does things like create  "access copies" before or during ingest risks accidentally forking the workflow, and so strictly speaking, cannot be considered OAIS conformant.


## Summary

These three distict information flow patterns show that there are fully functional and widespread archival information flows that are not strictly OAIS conformant. This is not a problem with the arhives, but with the assumptions withing OAIS.  Each workflow has it's place, but it's important to be aware of the balance of benefits and risks of each approach. 

A backup that's never been tested is no backup at all, and while this usually applies to storage and replication, it also applies to our AIPs and DIPs.


[^1]: Unless you have a time machine. But in that case, you don't need to worry about digital preservation.

[^2]: A smaller risk with up-front processing is that it's also possible to make this process dependent on other factors within that _Ingest_ context, without realising it (e.g. some piece of software, or a database, or just a simple file). These potential sources of missed dependencies may only become obvious when we try to (re)create a new DIP that can replace the original one.

[^3]: Note that while this overall information flow of does match OAIS quite well, there are significant areas of divergence. For example, the composition of the different information packages does not quote line up with the OAIS definitions. The different ways of implementing information packages is another aspect of digital preservation that might benefit from the identification of different patterns of practice.
