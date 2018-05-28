---
title: "Up and Running with GPG"
author: "Michael Mitchell"
email: "mmitc@protonmail.com"
geometry: margin=.5in
fontsize: 12pt
---

\pagebreak

\begin{center}
\section{Introduction}
\end{center}

---

This guide covers creating PGP keys for asynchronous encryption with GPG. It also covers how to talk to people using the asynchronous encryption model and how that model works with GPG. This guide assumes you're using a relatively recent version of GPG as of January 1 2018.

### 1) Important Remarks:  

* PGP and by extension GPG are designed to provide the Confidentiality and Integrity of your message content. They are not designed to provide Security by Obscurity. Thus who your talking to, when you talk to them, and if they reply to you is public knowledge as far as PGP and GPG are concerned.

* Be truthful when answering the questions prompted to you by GPG. If you lie you could really cofuse the people you're trying to communicate with. 

* Set the expiration date of your keys to no more than 1 year. Especially if this is your first key pair.

\pagebreak

\begin{center}
\section{Creating a PGP key with GPG.}
\end{center}

---

### 1) Create a GPG Private/ Public keypair.

``` { .bash .numberLines startFrom="1" }
$: gpg --full-generate-key
```

Creating your Public/ Private key pair is very customizable. The recommended defaults are pretty good; 

* Use RSA/ RSA for the key type (should be option 1).

* 2048 is a fine key size but I personally use 4096.

* 1y is a good value for the key expiration date.

* After that, answer the prompts truthfully and logically.

* Use a strong password!

### 2) Finding your keys.

Now that you have create a public and private key pair, it's time to look at them.

~~~ { .bash .numberLines startFrom="1" }
$: gpg --list-secret-key youremail@domain.com
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

### 3) Recap.

Awesome. In this section, we have created a PGP public/ private key pair using GPG and have demonstrated how to view those keys within GPG.

\pagebreak

\begin{center}
\section{Sending your keys to people!}
\end{center}

---

It's cool that we can generate and display PGP keys created with GPG, but they're not really useful if we can't send them to anyone!

### 1) Exporting your Public PGP key

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

