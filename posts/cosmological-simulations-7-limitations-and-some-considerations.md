<!-- 
.. link: 
.. description: 
.. tags: astro/physics, Cosmology, Master Thesis, millennium, N-body, Python, simulation, imported
.. date: 2011-12-04
.. title: Cosmological simulations #7: Limitations and some considerations
.. slug: cosmological-simulations-7-limitations-and-some-considerations
-->

<strong>Limitations</strong>    
    
In the previous posts we encountered some of the limitations of cosmological    
simulations. Let's review these in detail.    
First, we can consider a simulation composed of a finite box in a bigger space but to represent a real system, this box shouldn't be isolated so we use the periodic boundary conditions (<a href="http://brunettoziosi.blogspot.it/2011/11/cosmological-simulations-2-how.html" target="_blank" title="Cosmological simulations #2: how?">here</a>). This means that all the space around the box is filled with images of the box itself: a particle that leaves the box from one side will come in    
from the opposite side.     
<!-- TEASER_END -->    
Second, the mass inside the box is not continuous. Instead, it is made by particles of mass of the order of $10^9$ solar masses. These particles represent collisionless fluid elements (made by a huge quantity of real particles) with a certain    
volume and can't be treated as solid spheres. When two simulation particles are    
separated by a distance smaller than the radius of the volumes they represents    
they must feel less than the force coming from the entire mass (thanks to the    
Gauss/Birkhoff's theorem). To do this we soften (read "we reduce") the force at    
such small scales (<a href="http://brunettoziosi.blogspot.it/2011/11/cosmological-simulations-2-how.html" target="_blank" title="Cosmological simulations #2: how?">here</a>). Third, time is not continuous and its discreteness was also treated (<a href="http://brunettoziosi.blogspot.it/2011/11/cosmological-simulations-4-moving.html" target="_blank" title="Cosmological simulations: #4: Moving the particles!">here</a>) with some    
criteria to decide the time steps.    
Until now, however, we haven't consider the effects of taking into account    
initial density fluctuations over a range of scales that is finite. In    
addition to this, the finite size of the box pose a limit on the force    
resolution, because fluctuations on scales bigger than the box side will not    
included in the simulation due to the way the Fourier transforms act on a    
period box. Some tests in literature show that the exclusion of small    
scales shouldn't affect too much large scales when they reach the non linear    
regime but this not holds for the exclusion of large scales, those scales bigger    
than the box side. Following Bagla, the large scale exclusion should not    
disturb the formation of small haloes but could change their distribution.    
This effect will appear as an underestimation of the correlation function. Bagla    
finds that the best way of quantifying the effects of long wave modes is to    
check whether including them in the simulation will change the number of    
massive haloes or not and this can be estimated using the Press-Schecther mass    
function.    
In Tormen&amp;Bertschinger (1996) the missing power on large scales will cause    
something like a statistical cosmic bias decreasing the number of high-density    
regions, the strength of the clustering and the amplitude of the peculiar    
velocities.    
Methods have been developed to take the missing "larger than the box" wave modes    
into account and we will have a look on these in a future post.    
    
<strong>Some considerations</strong>    
    
As we have seen (<a href="http://brunettoziosi.blogspot.it/2011/11/cosmological-simulations-1-why-and-what.html" target="_blank" title="Cosmological simulations #1: why and what?">here</a>) N-body cosmological simulations    
are useful to understand aspects of non-linear gravitational clustering,    
since it's not possible to carry out laboratory experiments in gravitational    
dynamics and the analytic models fail when the system reach the non linear    
regime, i.e. when the density contrast overcome the unity. Related with    
cosmological simulations there are a pair of aspects that Bagla underlines in its    
articles that interesting to consider.    
The first issue is whether or not the gravitational clustering    
erase memory of initial conditions. Is there a one-to-one correspondence between    
some characterization of initial perturbations and the final state?    
N-body simulations shows that gravitational clustering does not erase memory of    
the initial conditions, the final power spectrum is a function of the initial    
power spectrum and this relationship can be written as a one-step mapping and    
the functional form of this mapping depends on the initial power spectrum.    
However density profiles of massive haloes have a form independent of    
initial conditions but there is a considerable scatter in density profiles    
obtained from N-body simulations and it is difficult to state whether a given    
functional form is always the best fit or not. I must admit that these last concepts are not very clear to me at the moment, and that I trust Bagla but I will deepen them as soon as possible to be able to comfortably master them.    
The second question is if it is possible to predict the masses and distribution    
of haloes that form as a result of gravitational clustering.    
The initial density field is taken to be a Gaussian random field and for    
hierarchical models the simple assumption that each peak undergoes collapse    
independent of the surrounding density distribution can be used to estimate the    
mass function and several related quantities but N-body simulations shows that    
this simple set of approximations is incorrect. However, the resulting mass    
function estimation is fairly accurate over a wide range of masses. Merger rates    
can be thus computed using the extended Press-Schecther formalism. Modifying    
some of this assumption can lead to improved predictions.    
    
<em>References</em>:    
<ul>    
<li><a href="http://www.ias.ac.in/currsci/apr102005/1088.pdf" target="_blank" title="J.S. Bagla, Cosmological N-body simulation: Techniques, scope and status">J. S. Bagla, Cosmological N-body simulation: Techniques, scope and status</a></li>
<li><a href="http://adsabs.harvard.edu/abs/1991ComPh...5..164B" target="_blank" title="J.S. Bagla and T. Padmanabham, Cosmological N-body simulations">J.S. Bagla and T. Padmanabham, Cosmological N-body simulations</a></li>
<li><a href="http://iopscience.iop.org/0004-637X/472/1/14" target="_blank" title="G. Tormen and E. Bertschinger, Adding long wavelenght modes to an N-body simulation">Giuseppe Tormen and Edmund Bertschinger, Adding long wavelenght modes to an N-body simulation</a></li>
<li><a href="http://adsabs.harvard.edu/full/1997MNRAS.286...38C" target="_blank" title="S. Cole, Adding long-wavelength power to N-body simulations">S. Cole, Adding long-wavelength power to N-body simulations</a></li>
</ul>
