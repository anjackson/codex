---
---

# Environments & Communities

One of the biggest reasons different organisations need different tactics is that they are actually trying to accomplish very different things. They operate in very different environements, work with very different communities, and consequently have very different goals.

What kinds of environments do archives operate in? How does this affect the way things work, the communities the archive works with, and what we should preserve?

## The OAIS Environment

The [Open Archival Information System (OAIS)][^oais] presents a simple model for the environment an archive operates in:

```{glue:figure} oais_environment_dot
```

# Role

Postel's Wedge. Pipe or Producer. 


## Kinds of Environment

Audiences, internal archive, enchanced care of the same to the same audence. e.g. BBC Archive.


### Direct 

![Space-time plot visualising events in the OAIS environment pattern.](./images/spacetime-context-direct.png)

Crucially, this means the DIP is generated from the AIP...

Pipeline versus sidecar preservation

POINT: If your not generating your DIP from your actual AIP you’re not doing OAIS.

Use digitised images as example. Look at risks of the sidecar approach. 



### Backup (via the publisher)

![Space-time plot visualising events in the 'backup' environment pattern.](./images/spacetime-plots-context-backup.png)

### Failover (via the published record)

![Space-time plot visualising events in the 'failover' environment pattern.](./images/spacetime-plots-context-failover.png)



[^oais]: https://public.ccsds.org/pubs/650x0m2.pdf




## Space-Time Diagrams

Visualising events and processes over time

I wanted a clear way to visualise events over time when talking about how we do digital preservation.  As my background is in physics, I wondered whether a simple version of a space-time diagram would work.

While these diagrams are mostly used in [relativity](https://en.wikipedia.org/wiki/Minkowski_diagram) and [quantum mechanics](https://en.wikipedia.org/wiki/Feynman_diagram), they can also be used to visualise simple physical systems, as shown below:

![Examples of space-time plots, visualising simple physical systems.](./images/spacetime-plots-intro.png)

As you can see, if an object is not moving, then it traces our a simple line parallel with the time axes.  If the object is moving through space, then the line runs at an angle -- the steeper the line, the faster the object is moving. If you plot two objects colliding, then the lines converge until the two objects start to bounce off each other. The lines then curve away until the two objects are heading in opposite directions.

While the events in the history of a digital archive behave very differently, a space-time diagram still provide a useful way of visualising what's going on.

```{glue:figure} spacetime_oais_fig
:figwidth: 100%
:name: "spacetime_oais_fig"

Visualisation of the basic OAIS workflow as a space-time trajectory.
```

See {doc}`/patterns/contexts/contexts` for more examples.

Idea of generating space-time plots rather than making them by hand:

- Plot e.g. SIP/AIP/DIP trajectories, add annotations and tick marks for names and places.
- Highlight events [like the dots on these plots](https://matplotlib.org/3.3.0/gallery/text_labels_and_annotations/annotation_demo.html#using-multiple-coordinate-systems-and-axis-types)
- Highlight time periods [like this](https://datavizpyr.com/highlight-a-time-range-in-time-series-plot-in-python-with-matplotlib/)


# Engagement

Approaches to community and patterns of engagement.

Twist of tooling towards distancing users. 

Have you ever been frustrated at not being able to talk to a person?

Look at item pages from lots of instiutions, where's the Reference Desk?

## Surveillance Capitalism

Separate page?

"Monitoring Designated Community"

...
To successfully maintain access to digital resources, all the stakeholders involved need to be in a position to make informed decisions.


i.e. Patterns are

- Surveillance. Watching.
- Broadcast. Speaking, not listening.
- Engagement. one-to-one, still not listening.
- Discourse? Listening.

