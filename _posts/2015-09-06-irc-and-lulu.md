---
title: IRC and Lulu
description: >
  This is a workshop for HacSoc "OpenHacks".  Learn about the basics of IRC: how
  to log in, what the jargon means, and how to use it for fun and profit.
  Finally, meet our IRC bot "Lulu", and learn how to hack new features into it!
layout: presentation
theme: night  
---

{{site.startslide}}

# IRC and Lulu

OpenHacks 9/6/15

Stephen Brennan

{{site.endslide}}
{{site.startvertical}}
{{site.startslide}}

## What is IRC?

- **I**nternet **R**elay **C**hat
- A chat protocol used all over the world.
- Anyone connected to the same server can chat with others on it.
- We host our own [IRC server](http://irc.case.edu)!

{{site.nextslide}}

## What isn't IRC?

- Private!
    - Anyone can log onto IRC, and possibly log conversations.
- Facebook chat
    - IRC doesn't save messages for you.  If you're not connected, you may miss
      something.

{{site.nextslide}}

## So why should I use it?

- Great instant communication among HacSoc members.
- Good for getting quick answers.
- Create discussion channels for any topic or class.
- Good experience: some companies have internal company-wide IRC.
- Plus, it's fun!

{{site.nextslide}}

## Where do I sign up?

- There's no sign-up!  Just connect and go.
- Mibbit web client: <http://irc.case.edu>
- Download a client.
    - Windows: [HexChat](https://hexchat.github.io/)
    - Mac: [LimeChat](http://limechat.net/mac/)
    - Linux: XChat (gtk), or Konversation (KDE).
        - Get these from your package manager
    - iOS: I hear LimeChat has a mobile version
    - Android:
      [AndroIRC](https://play.google.com/store/apps/details?id=com.androirc)

{{site.endslide}}
{{site.endvertical}}

{{site.startvertical}}
{{site.startslide}}

## How does it work?

- First, you connect to the server (I'll cover that shortly).
- Then, you choose a *nickname*.  This is like a username.
    - IRC doesn't by default protect your nick.
    - I'll cover how to keep others from using it.
- Next, join some *channels*.  These are just "chat rooms".

{{site.nextslide}}

## Connecting

- Server: irc.case.edu
- Port: 6697
- Use SSL? Yes.
    - If you see an option to accept invalid certificates, enable it.  If you
      see warnings about invalid certificates, ignore them (sorry!).

{{site.nextslide}}

## Choosing a nick

- Your client may offer a textbox when you connect.
- Otherwise, use the command `/nick [your nickname here]`.
    - This is an IRC command!

{{site.nextslide}}

## IRC Commands

- Besides just sending messages to channels, IRC has some commands you can use.
- All clients allow you to do commands by starting your message with a `/`
  (forward slash).
- Many clients give you GUI options to run these commands.
    - I can't teach you every GUI, but I can teach you what the commands are.

{{site.nextslide}}

## Some commands

- `/list` - list all channels on the server
- `/join #channel` - joins the channel `#channel`
- `/part [#channel]` - leave a channel
- `/msg username message` - sends `username` a `message` directly (only they see
  it).
- `/me [message]` - "emote" your message.
    - EG: If I send `/me laughs`, the channel will see `brenns10 laughs`.

{{site.nextslide}}

## Keeping your nick safe

- "`NickServ`" prevents others from using your username.
- It associates a password with your nickname.
- `/nick [whatever-you-want]`
- `/msg NickServ register [password] [email]`
- `/msg NickServ set kill on`
- Each time you connect:
    - `/msg NickServ identify [password]`

{{site.nextslide}}

## Making it all easier

- Most clients make IRC very easy.
- They remember the channels you use.
- They can automatically set your nick.
- They can automatically identify you to `NickServ`.

{{site.endslide}}
{{site.endvertical}}
