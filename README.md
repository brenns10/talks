Talks
=====

This repository holds the slides for any talks I give (mainly, Hacker's Society
presentations, OpenHacks workshops, etc).  It's hooked up directly to my
website, so all presentations are viewable live with a web browser.  It uses
Jekyll and GitHub pages, in a way that I think is pretty cool.

Presentations are just "posts" as Jekyll calls them.  Each presentation is just
a file in the `_posts` directory.  You can create a presentation really easily
with my setup:

```
---
title: Example
layout: presentation
description: This is an example presentation.
---
{{ site.startslide }}
# Example

This is my example presentation.  I'm using markdown to write it.
* Bullet points are simple.
* [Links](/index.html) are concise.

> Blockquotes are effortless

    print('Syntax highlighting is easy!')
{{ site.endslide }}
```

Front Matter
------------

In the front matter, you have to set `layout: presentation`, as well as your
presentation's title and a description.  The description is used in the talk
listing.  You can additionally specify:

- `theme`: use any theme name in Reveal's [theme list][].  Only use the name,
  not the `.css` ending, or any filepath.  The default is `theme: solarized`.
- `highlight`: choose the syntax highlighting theme.  Choose from any of
  Highlight.js's syntax highlighting [themes][syntax] (anything under the
  "styles" directory).  Just use the name, no `.min.css` or anything else.  The
  default is `highlight: zenburn`.
- `remotes`: Set this to any value you'd like (`true` is a good choice) to allow
  the Remotes.io plugin, which lets you use a smartphone as a presentation
  remote by scanning a QR code.  Default is disabled.


Slides
------

To write your slides, you can use the following variables which expand into
HTML:

* `site.startslide` - mark the beginning of a slide
* `site.endslide` - mark the end of a slide
* `site.nextslide` - a short cut for `{{ site.endslide }}{{ site.startslide }}`.
* `site.startvertical` - start a vertical slide group
* `site.endvertical` - end a vertical slide group

They're a bit janky, but they get the job done.  I don't have too much support
"built-in" yet for more advanced usage of Reveal.js; I'll add it if I need it.

All of your content can be written in Markdown.  It's actually converted to HTML
by Javascript, not by Jekyll.  So keep in mind that each slide is essentially a
snippet of Markdown.  There are probably idiosyncracies that will result.  You
can do syntax highlighting using the normal triple-backtick notation of
Markdown.

You can do LaTeX by employing the double-dollar sign `$$\int_a^b f(x)
\:\mathrm{d}x$$` syntax that's normal with MathJax.  Not all of LaTeX is
perfectly supported under MathJax, so it's worth doing some previewing with
Jekyll before deploying!

Quirks
------

The Jekyll site is designed to run on `http://stephen-brennan.com/talks/`.  In
order to avoid duplicating too much of my website's content and style info, I
rely on stylesheets and other resources from the main repository.  I just copied
and modified the relevant layouts and includes into here.  There are a few
quirks that make using this a bit annoying, especially when doing `jekyll serve`
locally:

- The index page refers to stylesheets that aren't present when you're testing
  locally.  So, the index page will appear styleless and a bit ugly.  That's not
  a huge deal, but it's annoying.
- The index page constructs links to slides by concatenating `site.url` with
  `page.url`.  I had to do this to make sure that the links function properly
  when I deploy, but the downside is that when you preview locally, the links
  will take you out to `stephen-brennan.com`, not the local draft.

[theme list]: https://github.com/hakimel/reveal.js/tree/master/css/theme
[syntax]: https://cdnjs.com/libraries/highlight.js
