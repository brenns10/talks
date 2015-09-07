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

## Now that you know Python ...

... how do you make something exciting?

By using <del>other people's code</del> <ins>libraries</ins>!

{{site.nextslide}}

## The best Python libraries are ...

... the standard libraries!

- Useful basics:
  [`collections`](https://docs.python.org/3/library/collections.html),
  [`pprint`](https://docs.python.org/3/library/pprint.html),
  [`random`](https://docs.python.org/3/library/random.html),
  [`argparse`](https://docs.python.org/3/library/argparse.html),
  [`logging`](https://docs.python.org/3/library/logging.html),
  [`unittest`](https://docs.python.org/3/library/unittest.html).
- Basic networking: [`socket`](https://docs.python.org/3/library/socket.html).
- Reading/writing data:
  [`pickle`](https://docs.python.org/3/library/pickle.html),
  [`csv`](https://docs.python.org/3/library/csv.html),
  [`json`](https://docs.python.org/3/library/json.html).
- Concurrency: [`threading`](https://docs.python.org/3/library/threading.html),
  [`multiprocessing`](https://docs.python.org/3/library/collections.html).
- High-level: [`itertools`](https://docs.python.org/3/library/itertools.html),
  [`functools`](https://docs.python.org/3/library/functools.html),
- Utility: [`os`](https://docs.python.org/3/library/os.html).
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

{{site.endslide}}
