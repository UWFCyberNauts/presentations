---
title: "Up and Running with GPG"
author: "Michael Mitchell"
email: "mmitc@protonmail.com"
geometry: margin=.5in
fontsize: 12pt
output:  md
    variant: markdown+header_attributes
---

\pagebreak

\begin{center}
\section{Introduction}
\end{center}

---

This guide covers creating PGP keys for asynchronous encryption with GPG. It also covers how to talk to people using the asynchronous encryption model and how that model works with GPG. This guide assumes you're using a relatively recent version of GPG as of January 1 2018.

### 1. Important Remarks: {#1.1}

* PGP and by extension GPG are designed to provide the Confidentiality and Integrity of your message content. They are not designed to provide Security by Obscurity. Thus who your talking to, when you talk to them, and if they reply to you is public knowledge as far as PGP and GPG are concerned.

* Be truthful when answering the questions prompted to you by GPG. If you lie you could really cofuse the people you're trying to communicate with. 

* Set the expiration date of your keys to no more than 1 year. Especially if this is your first key pair.

\pagebreak

\begin{center}
\section{Creating a PGP key with GPG.}
\end{center}

---

### 1. Create a GPG Private/ Public keypair. {#2.1}

``` { .bash .numberLines startFrom="1" }
$: gpg --full-generate-key
```

Creating your Public/ Private key pair is very customizable. The recommended defaults are pretty good; 

* Use RSA/ RSA for the key type (should be option 1).

* 2048 is a fine key size but I personally use 4096.

* 1y is a good value for the key expiration date.

* After that, answer the prompts truthfully and logically.

* Use a strong password!

### 2. Finding your keys. {#2.2}

Now that you have create a public and private key pair, it's time to look at them.

~~~ { .bash .numberLines startFrom="1" }
$: gpg --list-secret-keys youremail@domain.com
~~~

In this example, we are attempting to list the secret key that belongs to youremail@domain.com. Replace youremail@domain.com with the email address you created your key with.

After running that command you should see something similar to:

![Secret Key List](img/secretkeylist.png){#f1}

In [Figure 1](#f1), we can see the email address that the private key belongs to, the size of the key (rsa4096), the date the private key was created, the day the private key will expire, and the trust level of the key ([ultimate]). The easiest way of finding your key is by using your email address.

~~~ { .bash .numberLines startFrom="1" }
$: gpg --list-keys youremail@domain.com
~~~

After running that command you should see something similar to:

![Public Key List](img/publickeylist.png){#f2}

In [Figure 2](#f2) we are listing the public key that corresponds with the private key we listed in [Figure 1](#f1). We did this by using our email address as a unique identifier. When listing public keys, we can see much of the same information we see when listing private keys.

### 3. Listing all teh keys! {#2.3}

One day, you might eventually have several different PGP keys for a single email address for a multitude of reasons. Listing your PGP key by your email address might become inconvienient at that point. It then becomes necessesary to list all the keys and filter down to the one you wan't by KeyID. 

~~~ { .bash .numberLines startFrom="1" }
$: gpg --list-keys --keyid-format=LONG 
~~~

After running this command, you might see something similar to what I see

![Public key ring LONG KeyID](img/publickeylistkeyidlong.png){#f3}

When running the GPG command with the ```--list-keys``` flag without any trailing email address, GPG will list every public key it has in its keystore. In [Figure 3](#f3) I ran the command with the ```--keyid-format=LONG``` flag which presented the id's of the keys in a Universally Unique way. The KeyID is the part immediately after 'rsa4096/'. That long string between the '/' and the date the key was created is the KeyID. Notice that for this command the only thing we changed from earlier is that I swapped my email address with ```--keyid-format=LONG```. 

Some notes:

* You may use SHORT instead of LONG in ```--keyid-format=```

* You can actually use ```--keyid-format``` in addition to an __email address__ to list the key(s) belonging to that email address with their keyID.

* You can use ```--list-secret-keys``` instead of ```--list-keys``` to list the private keys instead. Again you can use an email address to filter down to just that email addresses key.

### 4. Recap. {#2.4}

Awesome. In this section, we have created a PGP public/ private key pair using GPG and have demonstrated how to view those keys within GPG.

\pagebreak

\begin{center}
\section{Sending your keys to people!}
\end{center}

---

It's cool that we can generate and display PGP keys created with GPG, but they're not really useful if we can't send them to anyone!

### 1. Exporting your Public PGP key
[3.1]: #3.1

~~~ { .bash .numberLines startFrom="1" }
$: gpg -a -o youremail@domain.com.pub.asc --export youremail@domain.com
~~~

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

By using this command, we have exported our public PGP key and have readied it to be sent to people. How you send your key to other people is up to you and depends on how you can actually contact them. By far the securest way to send a PGP public key to someone is by meeting them in person and using a USB drive. Many times people are not able to meet these constraints so sending the PGP key through email or some other relatively unsecured manner is probably necessary. Because of this neccessity, when receiving or sending a PGP key, you will need to know that key's fingerprint to verify with the sender/receiver that the key you received/sent is actually the correct key. Fingerprint verification should be done over a different secured channel, over the phone, etc. If you have a web server where you can host your PGP Fingerprint publicly, or on another service where you can host the fingerprint, that might be a solution over making a phone call or if you don't have a secure channel already set up.

~~~ { .bash .numberLines startFrom="1" }
$: gpg --fingerprint youremail@domain.com
~~~

This command will allow you to fingerprint your public key using the email address you created with the key.

Alternatively, you can use the KeyID we found earleir in [Section 2-3](#3.1)
