---
title: "Python and Pie: Making a Twitter Bot"
description: >
  Have you ever wanted to learn Python, eat Pie, and make an awesome Taylor
  Swift themed Twitter bot? Well, get ready, because this talk should allow you
  to achieve all of those dreams!
layout: presentation
---

{{site.startvertical}}
{{site.startslide}}

# Make A Twitter Bot
### Python and Pie 2016

Stephen Brennan

{{site.nextslide}}

Prerequisites: basic Python

- Functions (keyword arguments)
- If, For, While
- Modules, Importing
- Installing packages with pip

{{site.nextvertical}}

## Twitter API

You'll need an account and some API tokens in order to make a Twitter bot.

{{site.nextslide}}

Log into the account you'll use for your bot, and go to
[apps.twitter.com](https://apps.twitter.com)

![alt]({{site.baseurl}}/images/pypie/pypie_01_apps.twitter.com.png)

Click "Create New App"

{{site.nextslide}}

Fill out the form - this is what I used:

<img src="{{site.baseurl}}/images/pypie/pypie_03_filled_out.png" height="600px">

{{site.nextslide}}

This should bring you to a page like this.  Click on the "Keys and Access Tokens" tab.

<img src="{{site.baseurl}}/images/pypie/pypie_04_created_censored.png" height="600px">

{{site.nextslide}}

Now you should be here.  Click "Create my access token"

<img src="{{site.baseurl}}/images/pypie/pypie_05_keys_censored.png" height="600px">

{{site.nextslide}}

Keep this page up, we'll be using these keys later on!

<img src="{{site.baseurl}}/images/pypie/pypie_06_access_token_censored.png" height="600px">

{{site.nextvertical}}

## Programmer's First Tweet

{{site.nextslide}}

Create a folder for this project with two files.  For example:

```
bot/
  secrets.py
  bot.py
```

{{site.nextslide}}

In `secrets.py`, paste in the Twitter keys like this:

```
API_KEY = 'Consumer Key Here'
API_SECRET = 'Consumer Secret Here'
ACCESS_TOKEN = 'Access Token Here'
ACCESS_TOKEN_SECRET = 'Access Token Secret Here'
```

{{site.nextslide}}

Install the Twitter module with pip!

```
$ pip install twitter
```

If you're having trouble with this step (it involves the command line), let me
know.

{{site.nextslide}}

Now open up Python.  We're going to send our first tweet!

```
$ python
Python 3.5.2 (default, Jun 28 2016, 08:46:01)
[GCC 6.1.1 20160602] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from secrets import *
>>> from twitter import Twitter, OAuth
>>> t = Twitter(auth=OAuth(ACCESS_TOKEN, ACCESS_TOKEN_SECRET, API_KEY, API_SECRET))
>>> t.statuses.update(status='Hello, world!')
```

Check your bot's Twitter page!

{{site.nextvertical}}

## Bot!

From here, you can start writing the bot in `bot.py`!

For presentation, I'll walk you through the code in my editor. You can also find
the code [here](https://github.com/brenns10/pypie15int/blob/master/bot.py).

Check the full version of the bot running [here](https://twitter.com/pyswizzle).

{{site.endslide}}
{{site.endvertical}}
