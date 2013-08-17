<!-- 
.. link: 
.. description: 
.. tags: astro/physics, code, Computer, Master Thesis, Python, imported
.. date: 2011-11-17
.. title: Python CLI and configuration file parser
.. slug: python-cli-and-configuration-file-parser
-->

One of the first things I needed writing the code for my thesis was the ability to read options and parameters both from a configuration file and from the command line. After some attempts I have found (at <a href="http://www.decalage.info/" target="_blank" title="http://www.decalage.info">http://www.decalage.info</a>) a file parser to read a configuration file and the Python library <a href="http://docs.python.org/dev/library/argparse.html" target="_blank" title="argparse">argparse</a> for the command line parsing. In addition I have modified the file parser and I've added a "variable container" object, inspired by some snippets found somewhere on the web.    
<!-- TEASER_END -->
I chose to first parse the configuration file and after the command line options: if it's necessary the command line options will overwrite the file options.    
Let's consider the code, fully commented.    
````python
import argparse
def parse_config(filename):    
    """Read the config file and store the variables into a dictionary.
    Thanks to http://www.decalage.info
    """
    mlogger.info("Reading config file.")

    COMMENT_CHAR = '#'
    OPTION_CHAR =  '='

    options = {}
    f = open(filename)
    for line in f:
        # First, remove comments:
        if COMMENT_CHAR in line:
            # split on comment char, keep only the part before
            line, comment = line.split(COMMENT_CHAR, 1)
        # Second, find lines with an option=value:
        if OPTION_CHAR in line:
            # split on option char:
            option, value = line.split(OPTION_CHAR, 1)
            # strip spaces:
            option = option.strip()
            value = value.strip()
            # store in dictionary:
            options[option] = value
    f.close()
    return options
````    

And this is the container for the variables, also clearly commented.    
````python
class Bunch(object):
    """Create a dictionary object containing all the initial variables.
    """

    def __init__(self, d=None):
        if d is not None: self.__dict__.update(d)

def var(filename):
    """Read the initial variables and return a dictionary object.

    Parameters
    ==========

    filename = string, the name of the config file

    Returns
    =======

    Bunch(locals()) = dictionary object containing the local variables

    """

    # Read the config file and create a dictionary.
    options = parse_config(filename)

    # Common variables.
    mlogger.info("Defining common parameters.")

    parameter_1 = options['parameter_1']
    parameter_2 = options['parameter_2']
    parameter_3 = None
    option_1 = False

    return Bunch(locals())
````    

Now the commented code for the command line parsing.    
````python
# Read the configuration file.
    v = mod.var('../config.txt')

    # Check if there are CLI arguments, if yes start parsing.
    if argv is None:
        # Check for CLI variables.
        argv = sys.argv

        # Create the parser object.
        parser = argparse.ArgumentParser()

        # Create the parser entry.
        parser.add_argument('-p1', '-parameter_1', '--parameter_1', action='store', dest='parameter_1', default=v.parameter_1, 
                    help='Parameter 1 description')
        parser.add_argument('-p2', '-parameter_2', '--oparameter_2', action='store', dest='parameter_2', default=v.parameter_2, 
                    help='Parameter 2 description')
        parser.add_argument('-o', '--option', action='store_true', dest='option', default=None, 
                    help='Oprion description')

        # Add the parsed variables to a container object
        cli = parser.parse_args()

        # Overwrite the config file parameters
        v.parameter_1 = cli.parameter_1
        v.parameter_2 = cli.parameter_2
        v.option = cli.option

    elif isinstance(argv, dict):
        # Reading variables passed to Main as a function (Guido docet
        # http://www.artima.com/weblogs/viewpost.jsp?thread=4829).
        for i in argv.keys():
            if i in ("-p1", "--parameter_1"): 
                v.parameter_1 = argv[i]
            elif i in ("-p2", "--parameter_2"): 
                v.parameter_2 = argv[i]
            elif i in ("-o", "--option"):
                v.option = True
            else:
                print "Wrong parameter passed to main function, exit!!!"
                sys.exit(1)
````    

The configuration file look like this:    
````python
# Short description of parameter 1
parameter_1 = value

# Short description of parameter 2
parameter_2 = None
````
