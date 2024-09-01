# Design Patterns For Digital Preservation

In digital preservation, it seems like every question has the same answer: 

_...it depends..._

But what does it depend on? What are the contextual factors that affect our decisions?

This site aims to draw out distinct design patterns, based on real-world examples of digital preservation in practice. These patterns, and the contextual factors they depend on, build a map of the landscapes we work in, and help us find our path.

```{note}
This is an experiment, and right now there's only a handful of articles, mostly drawing on my own experiences.

If you'd like to see more of this kind of thing, or less, or if you can share practical examples that either align or break these patterns, [please let me know!](about:contact)
```
## Introduction

The goal of digital preservation is to maintain access to digital resources over time. But what this means in any given context is difficult to determine. Many decisions need to be made: What kind of storage? What kind of system? Or systems? Which risks should we attempt to mitigate? How will we know what works? In the digital preservation community, this difficulty has caused a split between the universal and the specific.

Standards like the Open Archival Information Systems reference model can provide useful high-level frameworks, but cannot provide concrete guidance when it comes to how to actually implement a digital preservation program. At the other extreme, over the years the digital preservation community has done a good job of sharing information on local implementations and workflows (through conferences like [iPres](https://ipres-conference.org/), and via things the [Community Owned Workflows](https://coptr.digipres.org/index.php/Workflow:Community_Owned_Workflows) wiki). These individual reports are a rich source of information, but synthesising this information is a very difficult challenge for a newcomer to take on, as they are least well equipped to know how relevant or current any particular piece of work might be.

The [NDSA Levels of Digital Preservation](https://ndsa.org/publications/levels-of-digital-preservation/) have helped bridge this gap from the top down, by providing a concrete roadmap of goals. But any such universal path necessarily must remain abstracted away from the details that depend on context. 

And working from the bottom up, summaries of recent work, like the [Digital Preservation Coalition's Technology Watch Publications](https://www.dpconline.org/digipres/discover-good-practice/tech-watch-reports) provide very helpful in-depth summaries of known areas of interest.  But this is still a lot to work through, and it remains difficult to quickly find and filter through the wide range of information on different approaches, and understand how the details depend on your context. 

The goal of this site is to build a bridge between the universal and the specific, and understand how our work should adapt to our context.


## Who is this for?

This site can help you preserve and maintain access to digital resources, whether you are handling digitised versions of print materials or born-digital content. But it is intended for people who already know a bit about digital preservation and have some degree of familiarity with the core concepts and terminology.

However, if you are just starting out, here are some recommendations that I think should help:

For a high-level overview, the [Wikipedia page on digital preservation](https://en.wikipedia.org/wiki/Digital_preservation) is pretty good, and [Ashley Blewer's](https://ashleyblewer.com/) [training slide decks](https://training.ashleyblewer.com/) (especially the [slides on Digital Preservation](https://training.ashleyblewer.com/presentations/digital-preservation.html#2), the [Open Archive Information System (OAIS) standard](https://training.ashleyblewer.com/presentations/oais.html#2) and ['fixity'](https://training.ashleyblewer.com/presentations/fixity.html#2)) provide a good introduction to some of the key terminology.  

The [Digital Preservation Coalition (DPC)](https://www.dpconline.org/) provide more [detailed resources](https://www.dpconline.org/digipres/what-is-digipres) like the [Digital Preservation Handbook](https://www.dpconline.org/handbook), while maintaining a keen focus on practical issues. 

I also _strongly_ recommend reading [The Theory and Craft of Digital Preservation](https://jhupbooks.press.jhu.edu/title/theory-and-craft-digital-preservation) by [Trevor Owens](http://www.trevorowens.org/), particularly for those with a background in cultural heritage ([see here for the open access version](https://osf.io/preprints/lissa/5cpjt/)). This book does an excellent job of framing digital preservation as a craft to be honed, and positions these practices in the wider cultural heritage context while providing a concrete framework for making progress.

Curiously, there does not seem to be many equivalent publications for those coming to digital preservation from the information technology side [^itbooks] -- but be warned, even if you know a lot about IT, digital preservation requirements can be seem strange at first. These communication issues are usually more subtle than they seem, so be prepared to clarify what you mean by terms like 'archive'!

[^itbooks]: Any suggestions are very welcome!

## What Are Design Patterns?

I first came across the idea of design patterns in the context of object-oriented software development. They have been very successful in that field, where [commonly used language and concepts](https://en.wikipedia.org/wiki/Software_design_pattern) can be traced back to the influential 1994 book [Design Patterns: Elements of Reusable Object-Oriented Software](https://en.wikipedia.org/wiki/Design_Patterns).

Crucially, these are not presented as _universal_ best practices, but rather as different ways of solving the same problem, along with a discussion of the pros and cons in various situations.[^1]  There are different patterns for how to 'solve' object creation, structure and behaviour, but the choice of which pattern to adopt is left to the reader to decide, based on their context. It's a toolbox, not a prescription.

This is the kind of approach I am attempting to apply to digital preservation. However, we must also recognise that we are at a earlier stage of development. The patterns are not yet clear, so I am trying to gather together the different ways we have solved our shared digital preservation problems, and see what patterns emerge.

The other main difference with software design patterns is the immense range of problems to be solved at different levels of granularity. From organisational structures and policies all the way down to storage design, digital preservation depends on many distinct layers of practice and technology. A single set of patterns can't cover everything at once.

Fortunately, the history of design patterns indicates a how we might be able to proceed. The original authors of the  _"Design Patterns"_ book were inspired by the idea of [pattern languages](https://en.wikipedia.org/wiki/Pattern_language).  This more complex framework proposes that large sets of patterns can form a kind of language with it's own grammar, and was first proposed in [A Pattern Language: Towns, Buildings, Construction](https://en.wikipedia.org/wiki/A_Pattern_Language) in 1977.

This applied the idea to the design of towns and communities, documenting a [cascading hierarchy of patterns](https://web.archive.org/web/20220319012035/http://www.patternlanguage.com/labyrinth/apl-tour2.html) to be considered when carrying out any kind of building project.  From _"Major structures which define the city"_ through _"Housing"_ and right down to things like _"Fix the exact positions for openings and frame them"_, these sets of patterns can be approached at any level.  As well as offering options in each case, the discussion explores how those choices interact with other sets of patterns, usually with the levels immediately above and below.

This is also similar to the idea of [Shearing Layers](https://en.wikipedia.org/wiki/Shearing_layers) in building design, where the different layers of design in a building are separated not just by physical size, but by how quickly each layer changes over time.  For example, the furniture might move around on a daily basis, while the layout moves more slowly, and the structure of the building only changes on rare occasion.

Taking _pattern languages_ and _shearing layers_ as inspiration, the plan is to look for different sets of design patterns in digital preservation, separated by granularity in terms of scale and rates of change. Ideally, it should be possible to start at any point in the hierarchy, while accepting that some cross-referencing may be required when discussions depend on patterns in neighbouring layers. However, as the patterns are still in the early stages of development, they will likely make more sense if read in the order shown here: starting at larger scales and then zooming in.

[^1]: The excellent DPC blog post [_When is 'good' better than 'best'? In support of digital preservation good practice_](https://www.dpconline.org/blog/when-is-good-better-than-best-in-support-of-digital-preservation-good-practice) does an excellent job describing the issues around "best practices" in more detail.