---
jupyter:
  jupytext:
    formats: ipynb,md
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.2'
      jupytext_version: 1.8.0
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
---

# The Plan

In _Foundations_, I'll cover a few crucial concepts which I believe are universally applicable to digital preservation, whatever context you work in. 

I'll then build on these concepts to describe the different digital preservation _Patterns_ I've found, mapping out how context affects preservation goals and tactics. 

Each pattern has been sythesized from a set of practical experiences, examples of which are evidenced in the _Practices_ section.


## Interactive notebooks

This site uses the [Jupyter Book](https://jupyterbook.org/) system, which means I can use [Jupyter Notebooks](https://jupyter.org/) to mingle prose and programming together. This is used to generate illustrations as well as provide concrete examples. You won't need to be able to understand the code to make sense of things, but they are easy to run and play about with if you're curious.

Here's a simple example, showing the frozen output of a simple command:

```python
print("Hello world...")
```

As it is, it can't _do_ anything. It just shows what was done.

To make it possible to re-run it, you can click the little rocket icon at the top of the page and choose where to run the [Jupyter notebook](https://jupyter.org/) that corresponds to the current page. This brings up a menu that looks like this:
 
 ```{image} ../images/launch-this-page.png
:alt: Launch This Page
:width: 250px
:align: center
```

I recommend using the [Binder](https://mybinder.org/) option, but note that any edits you make there cannot be saved (easily). If you have a Google account then the [Google Colaboratory](https://colab.research.google.com/) can be handy as on there the notebooks can be saved and indeed edited collaboratively. 

Either way, you should end up with a _'live'_ copy of a page that you can play with.


## Feedback

If you have any feedback about this site, you can contact me:

- on Twitter [@anjacks0n](https://twitter.com/anjacks0n)
- or via [email](mailto:anj@anjackson.net)

## Where to begin?

Well, before getting into technicalities, lets take a look around {doc}`/foundations/01-the-village`.

