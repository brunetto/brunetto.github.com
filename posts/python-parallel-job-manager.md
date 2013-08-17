<!-- 
.. link: 
.. description: 
.. tags: astro/physics, code, Computer, Master Thesis, Python, imported
.. date: 2011-11-04
.. title: Python parallel job manager
.. slug: python-parallel-job-manager
-->

The final version of the code for my master thesis was the most embarrassing parallel code you can think... just a serial code to be run on different slices of the dataset. I choose this solution because it permits to manage the different resources (memory, processors, ...) on the different machines available without any restriction. Moreover, this solution has no communication between the processes, with better performances and all the processes are independent, so it minimize the damages due to any failure.<br />
<!-- TEASER_END -->

At this step, however, I didn't know how to manage the different processes in a comfortable way. 
My requirements were:    

* to start only one process that will take care of starting the right code on the right data-slice
* the possibility to start "n" processes depending on the number of processors and memory available (in the actual code this is done by hand)
* the code should be able to start a new process when one of the previous processes end

Hereafter I expose and comment the complete "template" for this Python code as I wrote it.

```python
#!/bin/env python

import sys, os
from subprocess import Popen, PIPE
from multiprocessing import Process, Queue

"""This script starts n_procs processes that in parallel take the
number of the data file from a common queue and with a loop apply the
analysys code to the data starting it with a bash command using Popen
"""
````

The first line is the declaration of the interpreter to be used for this script, in this case Python. After that we import some libraries and modules used in this code. The last lines, inside the triple quotes, are the documentation string of the code. Python in fact has a self-doc system that can be used to understand what a piece of code does and how it works.

````python
n_procs = 10 # number of processes to be started
file_1 = None
file_2 =  "mill2_fof_sorted.h5"
m_factor = 1    # How many random more than data
start_slice = 0 
end_slice = 99
````
Here we set some parameters: the number of processes to start (set by hand), the two files to use in the analysis, how many random particles we use more than the data particles and the limits in the data slice to analyze. In this case we want to correlate the data in <code>mill2_fof_sorted.h5</code> with the data contained in the slices between slice 0 and slice 99. file_1 will be replaced after with the right name. This analysis will be carry out using 10 processes at each time. As a process end the code will take care of starting a new process.<br />
<pre>def starter(input, output):
    """Start the code processes one after the other"""
    while input.qsize() != 0:
        item = input.get()
        file_1 = "mill2sort-"+str(item[0])       
        cmd = "/opt/epd-7.0-2-rh5-x86_64/bin/python -u \
              ../serial.py --file_1 "+file_1+" --file_2 "+file_2+\
            " -l 400 -n 0 --m_factor "+str(m_factor)+" \
             --slicing --log ../logs/"+file_1+"-"+file_2

        try:
            pid = os.getpid()
            pid_cmd = 'echo "'+str(item[0])+'" &gt;&gt; '+str(pid)+'.log'
            os.system(pid_cmd)
            p = Popen(cmd, shell=True, close_fds=True).wait()

        except:
            print "Popen/os.system not done, exit..."
            sys.exit()</pre>
<br /></div>
<br />
This piece of code defines the function that will start the processes. It's called <code>started</code> and it takes <code>input</code> and <code>output</code> as arguments. These are two "queue objects", they can be filled and emptied in the FIFO way. The starter has a while loop that check if the queue is empty, if not it takes the next elements. This is the number of the slice to be used by the analysis code and with it we build the name of the file to be opened. <code>cmd</code> is the string we use to start the analysis code with some options (<code>serial.py</code> is the actual "cool" name I gave to my code!:P).<br />
The <code>try-exept</code> syntax is the particular Python way to manage the possible errors in the execution, giving the ability to the programmer to handle possible problems (exceptions).<br />
So we catch the pid of the starter and save into its log the number of sliced it start and pass to the <code>Popen</code> (process-open) command the string to start the analysis process telling it to wait the end of the process. If something goes wrong we print that there were some errors and exit the code in a clean way.<br />
<pre></pre>
<pre>def fill_queue(task_queue, start_slice, end_slice):
    """Fill the queue"""
    for i in range(start_slice, end_slice, 1):
        task_queue.put([i])
    return task_queue</pre>
<br />
This functions only fill the queue with the number of the sliced to be used.<br />
<pre></pre>
<pre>def status(proc):
    """Check for processes status"""
    if proc.is_alive()==True:
        return 'alive'
    elif proc.is_alive()==False:
        return 'dead'
    else:
        return proc.is_alive()</pre>
<br />
This piece of code check the status (dead or alive) of one process (<code>proc</code> is the process object... yeah, in Python everything is an object!)<br />
<pre>input_queue = Queue()
output_queue = Queue()

try:
    input_queue = fill_queue(input_queue, start_slice, end_slice)
except:
    print "Queue not filled, exit..."
    sys.exit()

procs = []    # processes container</pre>
<br />
Now we create the empty queues and (try to) fill them, and create the container for the processes objects.<br />
<pre>try:
    for i in range(n_procs):
        print "Process loop ", i
        procs.append(Process(target=starter, args=(input_queue, output_queue)))
except:
    print "Creating processes not complete, exit..."
    sys.exit()

try:
    for i in procs:
        i.start()
except:
    print "Start processes not complete, exit..."
    sys.exit()

for i in procs:
    print "Process ", i," @ " , i.pid, " is ", status(i)</pre>
<br />
This is the central part of this code: we create the processes objects and put them into the container, start them and check for their status. Everything is inside the <code>try-except</code> environment to check for possible errors and handle them.<br />
In practice we start "n" processes and every process take the number of a slice from the queue and use it to start the analysis code, waiting for its end. When the analysis is finished it takes another number from the queue and start again the code. When the queue is empty everything is automatically switched off.<br />
Future improvements will consider the automatically detection of the hardware resources and the possibility to mail the status of the code.

