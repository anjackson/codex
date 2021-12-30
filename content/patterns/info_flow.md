# Information Flow

The [Open Archival Information System (OAIS)](https://en.wikipedia.org/wiki/Open_Archival_Information_System) reference model is generally very high-level, and there are a lot of different possible ways of running an archive that would still fit. 

```{glue:figure} oais_environment_dot
:figwidth: 100%
:name: "oais_environment_dot"

```

However, one thing it is very clear about is the overall flow of information through the archive. 



## Flow Pattern 1: The Line


> OAIS §1.4 - CONFORMANCE:
> "A conforming OAIS Archive implementation shall support the model of information 
described in 2.2"
>
> OAIS §2.2.3 - INFORMATION PACKAGE VARIANTS:
> "Within the OAIS one or more SIPs are transformed into one or more Archival Information Packages  (AIPs)  for  preservation. [...] In response to a request, the OAIS provides all or a part of an AIP to a Consumer in the form of a Dissemination Information Package (DIP). "

In other words, Submission Information Packages (SIPs) come in from Producers, are managed as Archival Information Packages (AIPs), and then used to generate the Dissemination Information Packages (DIPs) that serve the needs of the archive's user community a.k.a. Consumers.

This fundemental design pattern for digital archives -- this way of describing the overall flow of archival information -- can be visualised via this simple diagram:


```{glue:figure} flow_line_dot
:figwidth: 100%
:name: "flow_line_dot"

```

This linear flow of information is one of the strengths of the OAIS model, because by generating the DIP from the AIP, we ensure that all the information we might need to (re)create a new DIP is in the AIP.

For an implementation to follow this pattern, it must ensure that the information in the SIP was _not_ used in the creation of the DIP. Ideally, the DIP should be generated from the AIP _post-ingest_, i.e. after the SIP has been discarded. This could be immediately after ingest, or some time later, or on demand.

### Examples

Here are some examples of digital preservation systems that enforce the OAIS information flow by generating access versions after ingest has been completed, referring only to the archived content.

#### The Internet Archive

The [Internet Archive](https://archive.org) documentation makes it clear that their archival system generates various derivatives for items after they have been ingested/uploaded. See for example this [documentation on type of derivatives they generate](https://help.archive.org/hc/en-us/articles/360014487651-Files-Formats-and-Derivatives-A-Basic-Guide), and this [summary table showing all the format conversions they do](https://archive.org/help/derivatives.php). Their web archive can generates access derivatives on demand, in much the same way as described in the next section. 

#### The UK Web Archive


For the subset of sites archived by the [UK Web Archive](https://www.webarchive.org.uk/) that are openly accessible, the overall process is similar to that used by the Internet Archive (and indeed most other web archives). The archived web resources are captured in [WARC files](https://en.wikipedia.org/wiki/Web_ARChive), which are placed on archival storage before the necessary indexes are generated from them in order to enable access. When individual items are requested, the relevant records are copied from the AIP and the access version is generated from the archival version during playback (dynamic requests and responses are indicated by arrows going on both directions).


```{glue:figure} flow_line_warc_dot
:figwidth: 100%
:name: "flow_line_warc_dot"

```

Note that while the overall information flow of most web archives does match OAIS quite well, there are significant areas of divergence. One example is that the composition of the information packages does not quote line up with the OAIS definition, hence the _SIP(ish)_ and _AIP(ish)_ labels in the above diagram. See _FIXME FUTURE SECTION(S) TO BE WRITTEN_.


## Flow Pattern 2: The Fork

The linear workflow described above may seem obvious, perhaps even inevitable, but it's not. While there is always a line from ingest to access[^1], there is sometimes a fork in the road.

```{glue:figure} flow_fork_dot
:figwidth: 100%
:name: "flow_fork_dot"

```

In this kind of forked workflow, both the AIP and the DIP are generated directly from the SIP. In contrast to the linear flow described above, this design pattern _does not automatically ensure_ that the AIP contains all the information we need to generate the DIP. This is not to say that this risk cannot be addressed, rather the point is that the implementation has to do _additional work_ to make sure that this is the case.

One of the reasons why this can happen is that, during the design and implementation of archival workflows, it is common to try and perform a lot of processing up-front. Schematically, the result can look something like this:

```{glue:figure} flow_fork_dip_ingest_dot
:figwidth: 100%
:name: "flow_fork_dip_ingest_dot"

```


Here I am using _Ingest_, _Store_ and _Access_ to identify processing contexts, covering all the functions associated with that phase of the workflow. In this example, during the _Ingest_ phase, the incoming packages have been used to generate the DIP prior to the finalisation of the AIP. Only after both have been created are they transferred to the appropriate storage.  This means it is _possible_ for the AIP and DIP to diverge.

In many cases, especially those where the critical payload of each package is a single file, this is a modest burden, because when the number of files involved is small, it's easier to keep track of individual files, their checksums, and their relationships. As things get more complex, it becomes easier for mistakes to be made.

Additionally, ensuring the AIP and DIP are stored together in a single coherent transaction also requires some care, in order to ensure that the stored items remain consistent through network and system outages.[^2]

These potential risks are certainly manageable - the point is simply that these risks arise because of the decision to perform more processing up front.  This does not mean "The Fork" is a _bad_ pattern to follow. Rather, it means we should be aware of the consequences of choosing this workflow pattern and make sure the benefits of up-front processing are worth the costs.

### Examples

#### An Outsourced Digitization

One real example involved a digitization project where much of the work had been outsourced to a third-party. The decision had been made to get the external partner to generate "access copies" as well as the long-term "preservation copies".

The preservation version consisted of high-resolution, full page TIFF files and associated metadata tying each set of TIFFs together, mapping back to the original publication. However, the access versions were not simply JPEG of the preservation versions, but were also broken up at the level of individual articles. This worked well for access purposes at the time of the project.

The problem was the segmentation process had not been properly documented. The coordinates on the TIFF version that corresponded to the positions of the JPEG versions had been lost. This meant that if the access copies become obsolete, it would not be possible to replace them like-for-like, i.e. while still preserving the same article-level experience. 

#### Normalization on Ingest

Many digital preservation systems offer NEED EXAMPLE




## Flow Pattern 3: The Stop

This final flow pattern addresses the dangers of "dark archives" - ones that cannot be accessed except by the people who manage the archive.

```{glue:figure} flow_stop_dot
:figwidth: 100%
:name: "flow_stop_dot"

```

In these cases, the focus tends to be on ingesting the content, and not on how that content might be used in the future. There may be DIPs, but no-one really uses them much. Or there may be no DIPs at all, or just some theoretical DIP based on an imagined future.

The danger here is that it's possible to miss some information you need from the SIP or from the wider context, because you'd only realise you needed it when your user community started trying to access the material.


### Examples

#### The UK Web Archive

While the UK Web Archive has thousands of open-access websites, we also archive many millions of sites under Non-Print Legal Deposit terms. This places heavy restrictions on access to those site, so 

'surrogate' access approaches.

#### The Forgotten Tapes

???

#### Access Copies

When access copies are generated at ingest time... 

#### The Preservation System

...


## Flow Pattern 3: The Split [???]

```{glue:figure} flow_sidecar_dot
:figwidth: 100%
:name: "flow_sidecar_dot"

```



## Conclusion

Like the backups you never tried to restore

Many preservation systems generate DIP components prior to ingest, and are therefore necessarily under _Flow Pattern 2: The Fork_. As such, the organizations that build their archives around these systems cannot be considered strictly conformant with the OAIS reference model.

AIP noun/verb, AIP is what it is, versus AIP the role it plays.


[^1]: Unless you have a time machine. But in that case, you don't need to worry about digital preservation.

[^2]: A smaller risk with up-front processing is that it's also possible to make this process dependent on other factors within that _Ingest_ context, without realising it (e.g. some piece of software, or a database, or just a simple file). These potential sources of missed dependencies may only become obvious when we try to (re)create a new DIP that can replace the original one.