<!-- 
.. link: 
.. description: 
.. tags: code, Master Thesis, imported
.. date: 2011-11-04
.. title: Loadleveler quick howto
.. slug: loadleveler-quick-howto
-->

Some useful commands to manage jobs with IBM `loadleveler` (`ll`).

First of all you need to write a script with some configuration options and the job to be submitted. You can call it (for example) "test_run.cmd". With this file you tell `ll` what you want to submit, the type of the queue, the directories you need, what you want to be logged and where, the number of parallel tasks and so on.
It would look like this:    

````bash
#!/bin/bash
# @ initialdir = /path-to-your-folder
# @ job_name = test_run
# @ output = test_run.$(jobid).out
# @ error = test_run.$(jobid).err
# @ notification = error
# @ class = long
# @ total_tasks = 20
# @ job_type = parallel
# @ queue

ulimit -s 65536

python ./start.py
````
<!-- TEASER_END -->

After that you can submit your job with `llsubmit test_run.cmd`.    

Other useful commands are    

* `llq -u $USER`: Return information about your jobs only in the queues
* `llq -l &lt;job&gt; `: Return detailed information about the specific
* `llq -s &lt;job&gt; `: Return information about why the job remains queued
* `llcancel &lt;job&gt; `: Cancel a job from the queues, either it is waiting or running
* `llstatus`: Return information about the status of the machine

<em>Reference</em>: <a href="http://hpc.cineca.it/content/batch-scheduler-loadleveler" target="_blank" title="Cineca LoadLeveler howto">Cineca LoadLeveler howto</a>