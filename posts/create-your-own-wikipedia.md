<!-- 
.. link: 
.. description: 
.. tags: diary, mediawiki, PhD, wikimedia, wikipedia, imported
.. date: 2012-03-26
.. title: Create your own Wikipedia
.. slug: create-your-own-wikipedia
-->

I was trying to find a tool to keep track of my activities (mainly), work activities. I've given a chance to some "diary" software but I was not convinced. I was lingering on using text files but it was not a solution. So I decided to try <a href="http://www.mediawiki.org/wiki/MediaWiki" target="_blank" title="Mediawiki homepage">Mediawiki</a>. And it was perfect!!!    
Now I'm going to describe the installation on an Ubuntu 11.10 with the repos packages.    

<!-- TEASER_END -->    

<strong>Packages installation</strong>    
    
First, install    

* `mediawiki`
* `Apache2`
* `mysql-server`
* `mysql-admin`
* `mysql-common`
* `mysql-client`
* `php5`
* `Imagemagick`
* `Latex`, if you want to display math

with Synaptic, Aptitude or whatever you want. In principle installing mediawiki all the rest will be installed as a dependence (except for `Latex`). Once you have installed all the packages you need to modify    

````bash
/etc/apache2/conf.d/mediawiki.conf
````
    
removing the comment (#) before     

````bash
Alias /mediawiki /var/lib/mediawiki
````
    
and then to restart Apache with     
````bash sudo /etc/init.d/apache2 restart
````
    
<strong>Database</strong>    
    
Start a root mysql prompt with    
````bash
mysql -u root -p
````
    
and create a database for your wiki:    
````bash
CREATE DATABASE dbname;
````
    
Then create a user with permissions for this database    
````bash 
GRANT ALL ON dbname.* TO 'user'@'localhost' IDENTIFIED BY 'password';
````
    
(pay attention to the "'").    
    
<strong>Wiki installation</strong>    
    
Go to `http://localhost/mediawiki` and follow the instructions!:)    
To be able to upload files and images you have to modify values in `/etc/mediawiki/LocalSettings.php`.    
    
<strong>XML dump</strong>    
    
To obtain a XMP backup of your wiki you can run:    
````bash
php /var/lib/mediawiki/maintenance/dumpBackup.php --full > $bck_path/$(date +"%F")-wiki_bck.xml
````
    
Note that `dumpBackup.php` works if you write into the database login where required.    
    
<em>Main references:</em>    
    
* <a href="http://framaulo.blogspot.com/2008/06/installare-ed-utilizzare-mediawiki-su.html" target="_blank">http://framaulo.blogspot.com/2008/06/installare-ed-utilizzare-mediawiki-su.html</a>
* <a href="http://www.ealmuno.com/2009/11/06/creare-database-in-mysql/" target="_blank">http://www.ealmuno.com/2009/11/06/creare-database-in-mysql/</a>
* <a href="http://ubuntuguide.org/wiki/MediaWiki_tips" target="_blank">http://ubuntuguide.org/wiki/MediaWiki_tips</a>


