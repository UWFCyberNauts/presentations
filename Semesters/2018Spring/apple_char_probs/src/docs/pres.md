---
title:
- Apple Vs. 1 Single Telugu Character
author:
- Michael Mitchell
theme:
- Copenhagen
---

# Apple Vs. Telugu

## Apple:

> "~~The most sophisticated mobile operating system~~"

>         - Apple 2k17

## Telugu:

\begin{center}
    \includegraphics[width=200px]{../img/meme1.jpg}
\end{center}

# What is all the fuss about?!
## Well...

\begin{center}
    \includegraphics[width=175px]{../img/info1.png}
\end{center}

>
>
>

\begin{center}
\textbf{21 bits UTF-8}
\end{center}

# What is Telugu and why should Apple care?

## Statistics
- ~15 most popular language on the planet
- For those that care: Dravidian language native to India
- 74 million speakers (as of 2001) in India
- India is the worlds 3rd largest smart-phone market

>
>
>

\begin{center}
\textbf{Kindof a big deal!}
\end{center}

# Demonstration time!

##

1. Look at any of the Wi-Fi connections available right now!
2. [https://www.youtube.com/watch?v=jPLfHEMDSu8](https://www.youtube.com/watch?v=jPLfHEMDSu8)

# Why is apple having a hard time?!

## Challenges of Unicode
- Unicode is HARD!
- UTF-8 [max of 21 bits](https://en.wikipedia.org/wiki/UTF-8)
- Characters in unicode can actually be phrases that form 1 character! (WOW)
- Zero-Width/ characters U+00200D
- Zero-Width Non-Joiner characters U+00200C
- Massive implementation

# Analyzing the content!

## Used rust cuz it's the best!
- Java can have a long dev time. Needed to be fast :D :P
- C is... C
- Rust has built in support for unicode (UTF-16)!
- Rust has a fantastic input preservation.
- Python could probably do it, but we're making a tool here, not a proof of concept!
- Find it here [https://tinyurl.com/yd9wwksh](https://tinyurl.com/yd9wwksh)

## 

\begin{center}
    \includegraphics[width=150px]{../img/meme2.jpg}
\end{center}

# The content
## UTF-8 characters

\begin{center}
    \includegraphics[width=200px]{../img/info2.png}
\end{center}

# What is it really?

## What it can't do:
- This isn't really an exploit, just an rendering bug.
- This does not **usually** cause permanent damange to a device.
- Doesn't gran't remote access
- Can't embed a virus

## What it **__could__** do:
- Empower orange hats to do their good stuff :D
- Behave as a kind of loopback DOS
- Create application crashes in iOS devices, possibly leading to exploit.
- Create system utility crashes in Apple devices, leaving the gate open to 
possibly priv-escalating into the process (brainstorming here)
- This "sign" character isn't the only character or language Apple is having problems with.

# Second to last slide, I promise!

## Mitigations
- Sprint is, as best as we can tell, slapping this out of the air as it flies.
- Change font from default
- UPDATE... Oh wait, Apple hasn't released the update yet!
- "Replace hardware" - Meltdown 2k17/18

## Usefulness
- Metasploit has something that allows you to automate this right? @Cody
- Bringing down a companies production.
- Raising H E double hocky sticks.
- Torment Zack and Justin

# THE END!

Buh Bye now!
