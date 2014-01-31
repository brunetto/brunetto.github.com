<!-- 
.. link: 
.. description: 
.. tags: 
.. date: 2014/01/31 16:46:42
.. title: Ssh keys exchange
.. slug: ssh-keys-exchange
-->

A superfast note on how to exchange ssh keys in order to connect without 
the need to remember a password.

On both the computer (`A` and `B`):

````bash
ssh-keygen
ssh-copy-id -i you@B
ssh you@B # to check if it works
````

