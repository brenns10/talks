---
title: The World of Python Packages
description: >
  A talk given at a HacSoc meeting in conjunction with Jeff Copeland.  Jeff gave
  an introduction to Python, and this 15-minute presentation gives an overview
  of the world of Python packages, the source of Python's power.
layout: presentation
---

{{site.startslide}}

# The World of Python Packages

Stephen Brennan

{{site.nextslide}}

## Now that you know Python...

... how do you make something exciting?

By using <del>other people's code</del> <ins>libraries</ins>!

{{site.nextslide}}

## Crash course in Python packaging

- TL;DR: `pip install package-name`
- Some packages need to be compiled first!
    - Read their documentation about how to install.
    - Windows users: check [here](http://www.lfd.uci.edu/~gohlke/pythonlibs/)
      for pre-built binaries.
    - Linux users: your package manager may have binaries.
- If you don't have root, try `pip install --user package-name`.
- Or, check out [Virtualenv](https://virtualenv.readthedocs.org/en/latest/).

{{site.endslide}}
