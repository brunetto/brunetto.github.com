<!-- 
.. link: 
.. description: 
.. tags: astro/physics, parallel, parameter, PhD, Python, imported
.. date: 2012-05-03
.. title: Parameter space parallel exploration in Python
.. slug: parameter-space-parallel-exploration-in-python
-->

Today a friend of mine ask me how to quickly and easily parallelize a parameter space exploration in his code. "Quickly and easily" means "do not try to use <a href="http://www.brunettoziosi.eu/blog/wordpress/phd-question-3-monte-carlo-markov-chain/" target="_blank" title="PhD question #3: Monte Carlo Markov chain">MCMC</a> or something similar!!!".     

<!-- TEASER_END-->    

I think a good solution could be use something like <a href="http://www.brunettoziosi.eu/blog/wordpress/python-parallel-job-manager/" target="_blank" title="Python parallel job manager">this</a> defining objects to contain parameters combinations and result, like this:    

````python
    class parameter(object):
      """Object to handle all the information about a parameter combination.
      """
      def __init__(self, a = None, b = None, c= None, d = None):
        """Construct parameters object."""
        self.name = str(self.a)+"-"+str(self.b)+"-"+str(self.c)+"-"+str(self.d)
        self.a = None
        self.b = None
        self.c = None
        self.d = None
        self.res_a = None
        self.res_b = None
        self.res_c = None
      def __repr__(self):
        return "" % self.name
````
and filling the queue in this way:

````python
    def fill_queue(input_queue):
      """Fill the queue"""
      parameter_set = [xrange(a_limit),xrange(b_limit), xrange(c_limit), xrange(d_limit)]
      # Create all possible combination of the parameters values and from these 
      # generate and put in the queue the objects
      for i in itertools.product(\*l):
        input_queue.put(parameter(i[0], i[1], i[2], i[3]))
      return input_queue
````
I think it's not optimal for a huge amount of combinations, because of the huge amount of objects, but in this case you can change the code to use lists or arrays. Anyway it should be better than four nested loops!:P
