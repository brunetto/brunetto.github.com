<!-- 
.. link: 
.. description: 
.. tags: code, Python
.. date: 2011-11-17
.. title: Python logging
.. slug: python-logging
-->

After I had a <a href="http://brunettoziosi.blogspot.it/2011/11/python-parallel-job-manager.html" target="_blank" title="Python parallel job manager">Python parallel job&nbsp;manager</a> I realize that all the attempts I have done to log what happen in my code weren't satisfying. It was not comfortable to manage every output when I want to change something and it was impossible to switch off some of logs without changing the code. The Python logging library is a great piece of code that permits to personalize most of the aspect of the logging in a program but maintaining a standard and comfortable interface. It also allows an easy management of many different outputs (file, screen, ...) and different levels of logging (error, info, ...) indipendent one from each other. It also allows to handle the logging of the imported modules.    
<!-- TEASER_END -->    
Here how I have used it.    
````python    
import logging
logger = logging.getLogger("Main_log")
logging.captureWarnings(True)
logger.setLevel(logging.DEBUG)
````
    
In the first line we import the module and tell it to handle also warnings coming from the Python interpreter or from other libraries. After that we set the minimum level of logging. In this way, if we want, for example, only the errors to be logged, every log below this level will be silenced.    
````python    
# Create file handler which logs even debug messages.
fh = logging.FileHandler(v.log_file+".log", 'w')
fh.setLevel(logging.DEBUG)
# Create formatter.
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
fh.setFormatter(formatter)
# Add the handlers to the logger.
logger.addHandler(fh)
if v.console is True:
	# Create console handler.
	ch = logging.StreamHandler()
	ch.setLevel(logging.DEBUG)
	ch.setFormatter(formatter)
	logger.addHandler(ch)
````
    
Now we create the object that will handle the log file, choose the level of logging and create an object that describe the format of the logs and apply it to the log handler. We also offer the possibility to have a console log handler.    
````python    
# Start logging.
logger.info("Log started.")
````
    
We start the logger and record the first log with log level "info".    
````python
mlogger = logging.getLogger("Main_log.modules")
````
    
This create the logger for one of the imported modules.    
