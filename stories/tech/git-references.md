<!-- 
.. link: 
.. description: 
.. tags: 
.. date: 2013/09/30 18:09:22
.. title: Git references
.. slug: git-references
-->

* [Ignoring files](https://help.github.com/articles/ignoring-files)
* [How to use GIT (easy)](https://speakerdeck.com/matze/distributed-version-control-and-why-you-want-to-use-it)
* [Good vs Bad Git usage](https://cwiki.apache.org/confluence/display/FLEX/Good+vs+Bad+Git+usage)
* [Git Book](http://git-scm.com/book)
* [Git tutorial](http://nyuccl.org/pages/GitTutorial/)

* Untrack files

````bash
git rm --cached file
````
* Remove files from all the repo history

````bash
git filter-branch -f --index-filter 'git rm --cached --ignore-unmatch filename' HEAD
````

* force a push

````bash 
git push origin master --force
````




