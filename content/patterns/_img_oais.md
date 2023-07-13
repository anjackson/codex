---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.5
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---


## Temporary Experimentation

```{warning}
The code blocks on this page are for **presentation** of code only, they are not executed.

For code execution, see the `{code-cell}` directive in the execution section of the documentation.
```

You can include code in your documents using the standard markup syntax of ` ```language `,
where language is the programming language for highlighting.

```python
import matplotlib.pyplot as plt

plt.plot([1, 2, 3], [1, 2, 3], 'go-', label='line 1', linewidth=2)
```

::::{tab-set}
:::{tab-item} Tab 1
:sync: tab1
Tab one
:::
:::{tab-item} Tab 2
:sync: tab2
Tab two
:::
::::

::::{tab-set}
:::{tab-item} Tab 1
:sync: tab1
Tab one (two)
:::
:::{tab-item} Tab 2
:sync: tab2
Tab two (two)
:::
::::

+++

# OAIS Diagrams

Diagrams relating to OAIS and information flows.

Note that only files included in the TOC are executed on build. This is just here for reference,

```{code-cell} ipython3
import graphviz
from myst_nb import glue

source = """
graph oais {
    rankdir=BT;
    
    node [color=Black,fontname=Arial,shape="box",style="rounded,filled",fillcolor="lightgrey:white", gradientangle=90,width="1.5",height="0.5"];
    
    man [label="Management"];
    
    nodesep=1;
    sip [label="Producer"];
    aip [label="OAIS\n(archive)", height="1.0"];
    dip [label="Consumer"];
    
    sip -- aip -- dip;
    man -- aip;
    
    {rank=same; aip, dip, sip}
}
"""
dia = graphviz.Source(source, format='svg')
glue("oais_environment_dot", dia)
```

## IF1: The Line

```{code-cell} ipython3
source = """
digraph oais_flow {
    rankdir=LR;
    
    node [color=Black,fontname=Arial,shape=box,style=filled,fillcolor="#eeeeee"];
    
    sip [label="SIP"];
    dip [label="DIP"];
    aip [label="AIP"];
    sip -> aip -> dip;
}
"""
glue("flow_line_dot", graphviz.Source(source, format='svg'))
```

```{code-cell} ipython3
source = """
digraph longtime_ingestdip {
    rankdir=LR;
    newrank=true;
        
    node [color=Black,fontname=Arial,shape=box,style=filled,fillcolor="#eeeeee"];
    edge [fontname=Arial];
    
    subgraph cluster_ingest {
        label="Pre-Ingest" fontname=Arial fillcolor="#ffffbf" style=filled color="#666666";
        isip [label="SIP"];
    }
      
    subgraph cluster_store {
        label="Store" fontname=Arial fillcolor="#ffffbf" style=filled color="#666666";
      saip [label="AIP"]; 
    }
    
    subgraph cluster_access {
        label="Use" fontname=Arial fillcolor="#ffffbf" style=filled color="#666666";
        adip [label="DIP"];
    }
    
    isip -> saip [label="Ingest"];
    saip -> adip [label="Access"];
}
"""
glue("flow_line_with_contexts_dot", graphviz.Source(source, format='svg'))
```

```{code-cell} ipython3
source = """
digraph warc_flow {
    rankdir=LR;
    
    node [color=Black,fontname=Arial,shape=box,style=filled,fillcolor="#eeeeee"];
    
    sip [label="WARCs & logs\n + metadata\n(SIP)"];
    aip [label="WARCs & logs\n + metadata\n(AIP)"];
    #idx [label="Indexes", shape="ellipse",fillcolor="#fbfbfb"];
    dip [label="Reconstructed\nweb pages\n(DIP)"];
    sip -> aip;
    aip -> dip;# [dir=both];
    #aip -> idx;
    #idx -> dip [dir=both];
    
}
"""
glue("flow_line_warc_dot", graphviz.Source(source, format='svg'))
```

```{code-cell} ipython3
source = """
digraph oais_ia_flow {
    rankdir=LR;
    
    node [color=Black,fontname=Arial,shape=box,style=filled,fillcolor="#eeeeee"];
    edge [fontname=Arial];
    
    sip [label="Item",fontcolor="gray"];
    dip [label="Item",fontcolor="gray"];
    aip [label="Item",fontcolor="gray"];
    sip -> aip [label="Upload"];
    aip -> dip [label="Derive"];
}
"""
glue("flow_line_ia_dot", graphviz.Source(source, format='svg'))
```

## IF2: The Stop

```{code-cell} ipython3
source = """
digraph fork_flow {
    rankdir=LR;
    
    node [color=Black,fontname=Arial,shape=box,style=filled,fillcolor="#eeeeee"];
    edge [];
    
    sip [label="SIP"];
    aip [label="AIP"];
    dip [label="DIP", color="gray",fontcolor="gray",fillcolor="#fefefe", style="filled,dashed"]

    sip -> aip;
    aip -> dip [style=dashed, color=grey];
}
"""
glue("flow_stop_dot", graphviz.Source(source, format='svg'))
```

## IF3: The Fork

```{code-cell} ipython3
source = """
digraph fork_flow {
    rankdir=LR;
    
    node [color=Black,fontname=Arial,shape=box,style=filled,fillcolor="#eeeeee"];
    edge [];
    
    sip [label="SIP"];
    dip [label="DIP"];
    aip [label="AIP"];

    sip -> aip:w;
    sip -> dip:w;
}
"""
glue("flow_fork_dot", graphviz.Source(source, format='svg'))
```

```{code-cell} ipython3
source = """
digraph longtime_ingestdip {
    rankdir=LR;
    newrank=true;
        
    node [color=Black,fontname=Arial,shape=box,style=filled,fillcolor="#eeeeee"];
    edge [fontname=Arial];
    
    subgraph cluster_ingest {
        label="Pre-Ingest" fontname=Arial fillcolor="#ffffbf" style=filled color="#666666";
        isip [label="SIP"];
        iaip [label="AIP"];
        idip [label="DIP"];
    }
      
    subgraph cluster_store {
        label="Store" fontname=Arial fillcolor="#ffffbf" style=filled color="#666666";
      sdip [label="DIP"];
      saip [label="AIP"]; 
    }
    
    subgraph cluster_access {
        label="Use" fontname=Arial fillcolor="#ffffbf" style=filled color="#666666";
        aaip [label="DIP",style=invis];
        adip [label="DIP"];
    }
    
    isip -> idip -> sdip;
    sdip -> adip [label="Access"];
    isip -> iaip;
    iaip -> saip [label="Ingest"];
    saip -> aaip [style=invis];
      
}
"""
glue("flow_fork_dip_ingest_dot", graphviz.Source(source, format='svg'))
```

```{code-cell} ipython3
source = """
digraph upstream_fork_flow {
    rankdir=LR;
    compound=true;
    
    node [color=Black,fontname=Arial,shape=box,style=filled,fillcolor="#eeeeee"];
    edge [];

    source [label="Source"]


    subgraph cluster1 {
      label="SIP";
      color=Black;
      fontname=Arial;
      shape=box;
      style=filled;
      fillcolor="#eeeeee";
      dip [label="DIP"];
      aip [label="AIP"];
    }

    source -> dip:w;
    source -> aip:w;
}
"""
glue("flow_fork_upstream_dot", graphviz.Source(source, format='svg'))
```

```{code-cell} ipython3
source = """
digraph encapsulated_fork_flow {
    rankdir=LR;
    compound=true;
    
    node [color=Black,fontname=Arial,shape=box,style=filled,fillcolor="#eeeeee"];
    edge [];

    sip [label="SIP"]

    dip [label="DIP"];

    subgraph cluster1 {
      label="AIP";
      color=Black;
      fontname=Arial;
      shape=box;
      style=filled;
      fillcolor="#eeeeee";
      sips [label="SIP",style="dashed"];
    }

    sip -> dip:w;
    sip -> sips:w;
}
"""
glue("flow_fork_encapsulated_dot", graphviz.Source(source, format='svg'))
```

## Backup vs Archive

```{code-cell} ipython3
source = """
digraph upstream_fork {
    rankdir=LR;
    
    node [color=Black,fontname=Arial,shape=box,style=filled,fillcolor="#eeeeee"];
    edge [];
    
    subgraph cluster1 {
      up [label="WIP"];
      dip [label="DIP"];
      up->dip;
    }
    
    subgraph cluster2 {
      sip [label="SIP"];
      aip [label="AIP"];
      adip [label="DIP", color=grey, fontcolor=gray, fillcolor="#f8f8f8"];
      color=invis;

      sip -> aip;
      aip -> adip [color=Grey, style=dashed];
    }

    up->sip [constraint=false];
    
    {rank=same; up sip}
    {rank=same; dip adip}
}
"""
glue("flow_sidecar_dot", graphviz.Source(source, format='svg'))
```

```{code-cell} ipython3

```
