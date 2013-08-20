<!-- 
.. link: 
.. description: 
.. tags: blogging, code, ipython, Nikola, Git, GitHub
.. date: 2013/08/18 01:29:57
.. title: Blogging with Nikola + Ipython + Git(Hub)
.. slug: blogging-with-nikola-ipython-github
-->

After a lot of different attempts now it seems that I'm able to run a static 
blog with Python, Nikola and Git.    

<!-- TEASER_END -->

The information are taken from:    
<ul>
<li> [http://www.damian.oquanta.info/posts/ipython-plugin-for-nikola-updated.html](http://www.damian.oquanta.info/posts/ipython-plugin-for-nikola-updated.html)</li>
<li> [http://diegoduncan21.github.io/posts/asi-lo-hice.html](http://diegoduncan21.github.io/posts/asi-lo-hice.html)</li>
<li> [https://github.com/yeoman/yeoman/wiki/Deployment](https://github.com/yeoman/yeoman/wiki/Deployment)</li>
<li> [http://stackoverflow.com/questions/12644855/how-do-i-reset-a-heroku-git-repository-to-its-initial-state](http://stackoverflow.com/questions/12644855/how-do-i-reset-a-heroku-git-repository-to-its-initial-state)</li>
<li> [http://cogumbreiro.blogspot.it/2013/05/how-to-install-git-subtree-in-ubuntu.html](http://cogumbreiro.blogspot.it/2013/05/how-to-install-git-subtree-in-ubuntu.html)</li>
</ul>

## Nikola

* first of all install some prerequisites:
````bash
sudo aptitude install python-virtualenv virtualenvwrapper libxml2-dev libxslt-dev
````

* export the environment path adding this line to `~/.bashrc`:
````bash
export WORKON_HOME=~/Envs
````
now the virtualenv are located in ~/Envs (you can choose another folder, of course)

* then create a virtualenv for the blog:
````bash
mkvirtualenv -p /usr/bin/python nblog
````

* enter the virtualenv with `workon nblog`

* run 
````bash
pip install nikola pyzmq tornado jinja2 requests sphinx markdown
````

* from the folder that will be the blog parent folder run
````bash
nikola init myblog
````

* list the themes and install a theme containing "ipython" into it
````bash
nikola install_theme -l to list all the available themes in Nikola
nikola install_theme jinja-site-ipython 
````

* modify your conf.py file adding the following lines to your `post_pages`:
````python
("posts/*.ipynb", "posts", "post.tmpl", True), ("stories/*.ipynb", "stories", "story.tmpl", False),
````
and make explicit to use the IPython theme:
````python
THEME = 'jinja-site-ipython'
````

* choose some options in the configuration file (your name, your blog name, if to gzip the files, 
add the search box, the disqus comments, if to use teasers and so on)

* to write a new post, just: 
````bash 
nikola new_post -f ipynb
````
or `-f markdown` to use the markdown syntax

* then, `nikola build` to build the site and `nikola serve` to see it
locally at [`localhost:8000`](localhost:8000)

## GitHub

Now we want to deploy the blog on the blogging platform GitHub Pages.
To do this you need a [GitHub](https://github.com/) account.    
Then    

* create a repository named `youname.github.com`

* install git locally and (if on Ubuntu 13.04) activate `git subtree` with
````bash
sudo chmod +x /usr/share/doc/git/contrib/subtree/git-subtree.sh
sudo ln -s /usr/share/doc/git/contrib/subtree/git-subtree.sh /usr/lib/git-core/git-subtree
````
if you are on an older Ubuntu version you can do [this](http://www.betaful.com/2011/01/i-love-git-subtree/):
````bash
git clone https://github.com/apenwarr/git-subtree.git
cd git-subtree
sudo bash ./install.sh 
# all this does is copies a file to your git folder, i.e. /usr/lib/git-core
````

* "git init" you blog with `git init` inside the main blog folder

* set the remote origin locally with
````bash
git remote add origin ssh://git@github.com/yourname/yourname.github.com.git    
````
I use ssh because I can log in without a password saving my key at 
[https://github.com/settings/ssh](https://github.com/settings/ssh)

* create an empty commit
````bash
git commit --allow-empty -am "first commit"
````

* now create the branch that will contain all the blog and move to it
````bash
git branch AllBlog
git checkout AllBlog
````

* add, commit and push the blog
````bash
git add ./*
git commit -am "first import"
git push origin master
````

* now you need to force the push of the files contained in the output folder to the master branch
in order to make the blog visible
````bash
git push origin `git subtree split --prefix output/ master`:master --force
````

* once you have done you can configure nikola to deploy the blog automatically 
modifying the deploy option in `conf.py`
````python
DEPLOY_COMMANDS = ["git checkout AllBlog",
				   "git add ./*",
				   "git commit -a",
				   "git push origin AllBlog",
				   "git subtree push --prefix output/ origin master"]
````

* now your workflow should be
````bash
nikola new_post -f ipynb
nikola build
nikola serve # optionally to check the output locally
nikola deploy
````
