<!-- 
.. link: 
.. description: 
.. tags:rsync
.. date: 2014/07/07 09:34:11
.. title: rsync like a pro
.. slug: rsync-like-a-pro
-->

To sync two folder on two different machines with a non-default ssh port:

````bash
rsync -avuh --progress --stats --rsh='ssh -p<your-ssh-port>' user@source:path user@dest:path
````

If you need it, `-c` flag will force files checksum to be sure they are the same or not. It takes a lot of time.


