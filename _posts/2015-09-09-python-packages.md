---
title: The World of Python Libraries
description: >
  A talk given at a HacSoc meeting in conjunction with Jeff Copeland.  Jeff gave
  an introduction to Python, and this 15-minute presentation gives an overview
  of the world of Python packages, the source of Python's power.
layout: presentation
---

{{site.startslide}}

# The World of Python Libraries

HacSoc 9/9/15

Stephen Brennan

{{site.nextslide}}

## Now that you know Python ...

... how do you make something exciting?

By using <del>other people's code</del> <ins>libraries</ins>!

This is a guide to Python's libraries.

Don't take notes, my slides are at:

<http://stephen-brennan.com/talks>.

{{site.nextslide}}

## The best Python libraries are ...

... the standard libraries!

- Useful basics:
  [`collections`](https://docs.python.org/3/library/collections.html),
  [`re`](https://docs.python.org/3/library/re.html),
  [`random`](https://docs.python.org/3/library/random.html),
  [`argparse`](https://docs.python.org/3/library/argparse.html),
  [`logging`](https://docs.python.org/3/library/logging.html),
  [`pprint`](https://docs.python.org/3/library/pprint.html),
  [`unittest`](https://docs.python.org/3/library/unittest.html).
- Basic networking: [`socket`](https://docs.python.org/3/library/socket.html).
- Reading/writing data:
  [`pickle`](https://docs.python.org/3/library/pickle.html),
  [`csv`](https://docs.python.org/3/library/csv.html),
  [`json`](https://docs.python.org/3/library/json.html).
- Concurrency: [`threading`](https://docs.python.org/3/library/threading.html),
  [`multiprocessing`](https://docs.python.org/3/library/collections.html).
- High-level: [`itertools`](https://docs.python.org/3/library/itertools.html),
  [`functools`](https://docs.python.org/3/library/functools.html).
- Utility: [`os`](https://docs.python.org/3/library/os.html),
  [`sys`](https://docs.python.org/3/library/sys.html),
  [`subprocess`](https://docs.python.org/3/library/subprocess.html).
- See the full list [here](https://docs.python.org/3/library/index.html).

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

{{site.nextslide}}

## Web development frameworks

- [Django](https://www.djangoproject.com/) - widespread MVC framework, used by
  Instagram, Pinterest, Disqus, Bitbucket, ...
- [Flask](http://flask.pocoo.org/) - small "micro-framework" for simple apps.
- [Tornado](http://www.tornadoweb.org/en/stable/) - scalable, non-blocking
  networking library that works well for web dev
- Other common names: Pyramid, Zope, Web.py

{{site.nextslide}}

## Wed development tools

- [Jinja2](http://jinja.pocoo.org/) - simple templating system for HTML (or any
  other text file)
- [MarkupSafe](http://www.pocoo.org/projects/markupsafe/) - HTML escaping!

{{site.nextslide}}

## Databases

- [Psycopg2](http://initd.org/psycopg/) - interface to PostgreSQL
- [sqlite3](https://docs.python.org/3/library/sqlite3.html) - standard library
  interface for small databases in local files
- [SQLAlchemy](http://www.sqlalchemy.org/) - widely used
  [object relational mapper](https://en.wikipedia.org/wiki/Object-relational_mapping),
  used by Dropbox, Hulu, reddit, Yelp, Uber, ...
- Django has a good built-in object relational mapper, too.

{{site.nextslide}}

## Web scraping

- [Requests](http://docs.python-requests.org/en/latest/) - the **only** way to
  make HTTP requests (e.g. download web pages).  Used by Amazon, Google,
  Twitter, Mozilla, PayPal, ...
- [lxml](http://lxml.de/) - parser for HTML and XML.  *Fast,* because it uses C
  libraries to do the heavy lifting
- [BeautifulSoup](http://www.crummy.com/software/BeautifulSoup/) - "parser" for
  *badly written* HTML.
- [Scrapy](http://scrapy.org/) - web scraping "framework" that lends itself to
  making crawlers.  Python 2 only :(

{{site.endslide}}
