---
title: C from Java
description: >
  C's syntax is dangerously similar to Java's, making it difficult to work with
  if you haven't spent much time learning about their differences.  This talk
  aims to bridge the gap for students taking CWRU's EECS 338.
layout: presentation
theme: night
---

{{site.startslide}}

# C from Java

Openhacks 9/20/2015

Stephen Brennan

{{site.endslide}}
{{site.startvertical}}
{{site.startslide}}

## First things first

{{site.nextslide}}

It's not safe to compile C without a Makefile!

Take [this](https://github.com/brenns10/last-makefile)!

It's Tekin-approved!  You can safely use it on your homework.

{{site.nextslide}}

## Why?

It automagically detects dependencies, so you don't have to edit your makefile
each time you add a `.c` file.

It sets the compiler to issue more warnings, so you catch more errors at compile
time, instead of runtime!  This has saved me hours of debugging, easily.

It has debug and release configurations, so you can (more) easily debug when you
have problems.

Many more things you may not need in EECS 338.

{{site.nextslide}}

## How?

1. Put it in your project root.
2. Fill out the variables at the top.
3. Put all your source files in the `src/` directory.
4. Run `make`.
5. Your program is at `bin/release/[name]`

{{site.nextslide}}

## For future reference

- Debugging:
    - `make CFG=debug`
    - `bin/debug/[name]`
- Variables...
  - `PROJECT_TYPE=executable`
  - You can leave `TEST_TARGET`, `STATIC_LIBS`, and `EXTRA_INCLUDES` alone.
- You should never need to `make clean`!

{{site.endslide}}
{{site.endvertical}}
{{site.startvertical}}
{{site.startslide}}

## Syntax

(just the differences)

{{site.nextslide}}

## Functions Don't Go In Classes

Since there are no classes in C, it's pretty difficult to have functions inside
of classes.

{{site.nextslide}}

## Declaring Structs

```c
struct customer {
  char *name;
  int id;
  unsigned int age;
  struct customer *child;
};
```

**Don't forget the semicolon at the end!**

Use it like this:

```c
struct customer mycustomer;
mycustomer.name = "Stephen";
// ...
```

{{site.nextslide}}

## Typedef

`typedef` allows you to create a new *name* for an *existing* type.  EG:

```c
typedef struct customer customer_t;
typedef unsigned int id_t;
typedef struct {
  char *destination;
  int id;
} bus_t;
```

- That last one allows you to use your structs without the `struct` keyword.
- It's common practice to end type names with `_t` so readers can tell they are
  types, and not any other identifier.

{{site.nextslide}}

## Static

*Forget what you know about it in Java.*

* `static` variables are stored in static memory.
    * I'll explain more about this in a bit.
* `static` functions can only be used in the file where they're defined.
    * Good for helper functions!

{{site.endslide}}
{{site.endvertical}}
