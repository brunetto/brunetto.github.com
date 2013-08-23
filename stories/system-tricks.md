<!-- 
.. link: 
.. description: 
.. tags: 
.. date: 2013/08/22 12:18:45
.. title: System tricks
.. slug: system-tricks
-->

## Searching

* `grep -H '<string>' *.<ext>`
* `grep -r "<strings>" ./`
* `sudo updatedb && locate <nomefile>`

## Download

* download music from youtube
````bash
youtube-dl --extract-audio --audio-format=mp3 <youtubeLink>
````
for example:    
.. listing:: YTdownload.py python