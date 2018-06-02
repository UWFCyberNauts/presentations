---
title: "Up and Running with GPG"
author: "Michael Mitchell"
email: "mmitc@protonmail.com"
geometry: margin=1in
fontsize: 12pt
linkcolor: blue
header-includes:
    \usepackage{fancyhdr}
    \pagestyle{fancy}
    \fancyhead[CO,CE]{Up and Running with GPG}
    \fancyfoot[CO,CE]{Written by Michael Mitchell for the UWF Cyber Security Club}
---

\renewcommand{\contentsname}{Table of Contets}

\tableofcontents

\pagebreak

# Introduction {#section1}

This guide covers creating PGP keys for asynchronous encryption with GPG. It also covers how to talk to people using the asynchronous encryption model and how that model works with GPG. This guide assumes you're using a relatively recent version of GPG as of January 1 2018.

## 1. Important Remarks {#section1-1}

* PGP and by extension GPG are designed to provide the Confidentiality and Integrity of your message content. They are not designed to provide Security by Obscurity. Thus who your talking to, when you talk to them, and if they reply to you is public knowledge as far as PGP and GPG are concerned.

* Be truthful when answering the questions prompted to you by GPG. If you lie you could really cofuse the people you're trying to communicate with. 

* Set the expiration date of your keys to no more than 1 year. Especially if this is your first key pair.

\pagebreak

# Creating Keys {#section2}

In this section we will cover how to create a PGP key pair using good secure defaults and how to see those PGP keys in GPG using a variety of methods

## 1. Your First Keypair {#section2-1}

``` { #e1 .bash .numberLines startFrom="1" }
$: gpg --full-generate-key
```

Creating your Public/ Private key pair is very customizable. The recommended defaults are pretty good; 

* Use RSA/ RSA for the key type (should be option 1).

* 2048 is a fine key size but I personally use 4096.

* 1y is a good value for the key expiration date.

* After that, answer the prompts truthfully and logically.

* Use a strong password!

## 2. Finding Your Keys {#section2-2}

Now that you have create a public and private key pair, it's time to look at them.

``` { #e2 .bash .numberLines startFrom="1" }
$: gpg --list-secret-keys youremail@domain.com
```

In this example, we are attempting to list the secret key that belongs to youremail@domain.com. Replace youremail@domain.com with the email address you created your key with.

After running that command you should see something similar to _[Figure 1](#f1)_

![Secret Key List](src/img/secretkeylist.png "Figure 1"){#f1}

In _[Figure 1](#f1)_, we can see the email address that the private key belongs to, the size of the key (rsa4096), the date the private key was created, the day the private key will expire, and the trust level of the key ([ultimate]). The easiest way of finding your key is by using your email address.

``` { #e3 .bash .numberLines startFrom="1" }
$: gpg --list-keys youremail@domain.com
```

After running that command you should see something similar to _[Figure 2](#f2)_

![Public Key List](src/img/publickeylist.png "Figure 2"){#f2}

In _[Figure 2](#f2)_ we are listing the public key that corresponds with the private key we listed in _[Figure 1](#f1)_. We did this by using our email address as a unique identifier. When listing public keys, we can see much of the same information we see when listing private keys.

## 3. All Teh Keys! {#section2-3}

One day, you might eventually have several different PGP keys for a single email address for a multitude of reasons. Listing your PGP key by your email address might become inconvienient at that point. It then becomes necessesary to list all the keys and filter down to the one you wan't by KeyID. 

``` { #e4 .bash .numberLines startFrom="1" }
$: gpg --list-keys --keyid-format=LONG 
```

After running this command, you might see something similar to what I see

![Public key ring LONG KeyID](src/img/publickeylistkeyidlong.png){#f3}

When running the GPG command with the ```--list-keys``` flag without any trailing email address, GPG will list every public key it has in its keystore. In _[Figure 3](#f3)_ I ran the command with the ```--keyid-format=LONG``` flag which presented the id's of the keys in a Universally Unique way. The KeyID is the part immediately after 'rsa4096/'. That long string between the '/' and the date the key was created is the KeyID. Notice that for this command the only thing we changed from earlier is that I swapped my email address with ```--keyid-format=LONG```. 

Some notes:

* You may use SHORT instead of LONG in ```--keyid-format=```

* You can actually use ```--keyid-format``` in addition to an __email address__ to list the key(s) belonging to that email address with their keyID.

* You can use ```--list-secret-keys``` instead of ```--list-keys``` to list the private keys instead. Again you can use an email address to filter down to just that email addresses key.

## 4. Recap {#section2-4}

Awesome. In this section, we have created a PGP public/ private key pair using GPG and have demonstrated how to view those keys within GPG.

\pagebreak

# Sending Your Keys! {#section3}

In this section I will cover how to export your PGP keys, how to send your public PGP key to someone, and how to verify that PGP key.

## 1. Exporting Your Public Key {#section3-1}

It's cool that we can generate and display PGP keys created with GPG, but they're not really useful if we can't send them to anyone!

``` { #e5 .bash .numberLines startFrom="1" }
$: gpg -a -o youremail@domain.com.pub.asc --export youremail@domain.com
```

Wow! Delving right in:

```-a```

export the encrypted content as ascii. This translates the raw bits and bytes of the ciphertext into something readable by modern text editors. This format is also more transportation friendly.

```-o```

write the public key to the file following the flag

```youremail@domain.com.pub.asc```

the file to write the public key to.

```--export```
    
export the public key denoted by the next argument

```youremail@domain.com```
    
The email associated with the public key you are trying to export.

## 2. Sending a Key {#section3-2}

Now that we have exported our public PGP key and have readied it to be sent to people, we must actually send it to people. There is a multitude of ways to do this. How you send your key to other people is up to you and depends on how you can actually contact them.

Here are some available options from most secure to least secure (all of these methods will work):

* Meet the recipient in person and give them a USB drive with your public PGP key. 

* Send them your key over a different secure method such as a prevously set up synchronous channel.

* Email them your key.

\pagebreak 

# Fingerprinting a Key {#section4}

When sending or receiving a PGP key you will need to know that key's fingerprint to verify with the sender/receiver that the key you received/sent is actually the correct key. Fingerprint verification should be done over a seperate secured channel, over the phone if you know what their voice sounds like, etc. If you have a web server where you can host your PGP Fingerprint or you can host the fingerprint on another service; one of those methods might be a solution over making a phone call, etc.

``` { #e6 .bash .numberLines startFrom="1" }
$: gpg --fingerprint youremail@domain.com
```

This command will allow you to fingerprint your public key using the email address you created with the key.

Alternatively, instead of using your email address to identify the key, you can use the KeyID method I identified earleir in [Section 2-3](#section2-3)

Running the above command may produce output similar to _[Figure 4](#f4)_:

![A Fingerprint of a Public PGP key](src/img/fingerprint.png){#f4}

Here the fingerprint is on the second line, the groupings of 4 characters made up of upper case letters and numbers. Use that fingerprint to verify your key with others.

\pagebreak

# Receiving keys! {#section5}

## 1. Importing a key {#section5-1}

The very first thing you need to do when receiving a PGP key is to import it into GPG so you can perform actions upon that key such as finding the fingerprint of that key. So far I have only elaborated how to get the fingerprint of __your__ key.

``` { #e7 .bash .numberLines startFrom="1" }
$: gpg --import publickey.gpg.asc
```

where publickey.gpg.asc is the public key file that someone has sent you and is the PGP public key in this example.

After you import the key, you should be presented with something similar to _[Figure 5](#f5)_

![Importing a PGP Public Key](src/img/importingPublicKey.png){#f5}

If you were to list a key you have just imported either by the email or long key ID shown to us by GPG, you will be presented with something similar to _[Figure 6](#f6)_

![Listing a Recently Imported Public Key](src/img/recentlyImportedPublicKey.png){#f6}

At this stage in the process of receiving a key, you would fingerprint the key you have imported and perform a fingerprint verification process so that you can determine if the key you have received is really the key that was intended to be sent to you by the sender. Remeber, since you have imported the key into GPG, you can use the same method for fingerprinting keys described in _[Section 4](#section4)_

## 2. Trusting keys {#section5-2}

In _[Figure 6](#f6)_ we can see that on the third line, there is [unknown] in brackets. This represents how much you have configured GPG to trust this key. By default, GPG will configure the trust level of a recently imported key to '[unknown]'. There are different trust levels that you can assign a key within GPG. These trust levels do not affect the key itself, only other keys that are signed by that key/keypair. The trust levels and what they do are in _[Table 1](#t1)_

Trust Level | Description
--- | ---
Ultimate | The Ultimate trust level is only intended to be used with __your own keys__
Full | This trust level is for keys you trust to __sign other keys__. I.E. if you import a key from Bob and trust if 'Fully', then if you receive a key from Alice that is signed by Bob's key, you can technically skip fingerprint verification because Alice's key has been cryptographically signed by Bob's 'Fully' trusted key.
Marginal | This will make any key you receive valid as long as it has been signed by three other keys. This is a fairly complex trust level that most recommend avoiding.
Unknown / Undefined | Technically both of these trust levels are the same, Unknown is set by GPG when importing a key, Undefined is set by a user usually to represent that they will come back to verify/ change it's trust level later.
Never | This trust level is programmatically identical to Unknown/ Undefined except that the user has actively chosen to __never__ trust the key in question. A good example of when to use this trust model would be when you import a key from someone whom you know to be siging other keys without accurately verifying those keys.

Ideally, after you have verified the key's fingerprint with the sender (now that the key is imported into GPG you can use the same method outlined in _[Section 4](#section4)_ to get that keys fingerprint) you can set the trust level of that key to something appropriate.

To trust a key, you will have to use the ```--edit-key``` flag with gpg.

``` { #e8 .bash .numberLines startFrom="1" }
$: gpg --edit-key youremail@domain.com
```
In _[Example 8](#e8)_ above, I tell GPG to edit a key by using an email address as a unique identifier. You may use a Key ID format instead of an email address to identify to GPG the key you wish to edit.

After calling the command to edit a key in GPG, you will be presented with a GPG console that you can use to trust a key in GPG. The console looks like _[Figure 7](#f7)_

![GPG Console to edit a PGP Key](src/img/gpgEditConsole.png){#f7}

To trust this key you have selected to edit, type ```trust```. You will then be presented with something similar to _[Figure 8](#f8)_.

![Trust Menu for a key in GPG](src/img/trustMenuGPG.png){#f8}

From here you choose the level of trust you wish to grant this key, then type ```quit```. You will then be put back to your regular command line.
>>>>>>> Stashed changes
