---
title: Test Presentation
layout: presentation
theme: night
description: >
  This is a presentation I'm writing just to show that I can!
---

{{ site.startslide }}
# Welcome!
{{ site.endslide }}

{{ site.startslide }}
### Example

This is an example presentation.  I'm using markdown to write it.

* Bullet points are simple.
* [Links](/index.html) are concise.

> Blockquotes are effortless

    print('Syntax highlighting is easy!')
{{ site.nextslide }}
### Typeset Math With MathJax

$$\int_a^b f(x) \: \mathrm{d}x$$
{{ site.endslide }}

{{ site.startvertical }}
{{ site.startslide }}
# I can do vertical slides!
{{ site.endslide}}

{{ site.startslide }}
# Woah
{{ site.endslide }}
{{ site.endvertical }}
