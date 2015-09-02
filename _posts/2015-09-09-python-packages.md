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

## What's in this talk

- Brief intro on packaging terms.
- Basics of installing packages.
- List of major Python packages and what you can use them for.

{{site.nextslide}}

## Python Packaging

- Sometimes a rough world.
- "Module" - a single ".py" file.
- "Package" - a folder of modules, with an `__init__.py`.
- "Pip" - Python's package manager.

{{site.nextslide}}

## Installing Packages

- Use Pip to install packages: `pip install package-name`
- Pip is best used on Linux, but can be used on Mac/Win.
    - You may need to configure your PATH!
- Some packages are "native", meaning they have parts written in C.
    - On Linux, these need to be compiled.  You may need to install packages in
      order for them to compile properly.  Check their documentation.
    - On Windows, you'll need to find a pre-built version.

{{site.nextslide}}

## Per-User and Virtual Environments

- Normally, Pip installs packages globally.  You need "root" to use it: `sudo
  pip install X`.
- On Linux (e.g. on the ACM People server), you can install packages per-user:
  `pip install --user X`.
- You can also create "virtual environments", which are small Python
  installations, usually dedicated for a single project.
    - `pyvenv-3.4 venv`
    - `. venv/bin/activate`
    - Now, `pip install` packages into the venv to your heart's delight.

{{site.endslide}}
