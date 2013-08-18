<!-- 
.. link: 
.. description: 
.. tags: astro/physics, n-body simulations, Cosmology, N-body, PhD, simulation, imported
.. date: 2011-11-29
.. title: Cosmological simulations #6: adding gas!
.. slug: cosmological-simulations-6-adding-gas
-->

As we have seen, cosmological N-body simulations consider only gravitational interactions. This is good for large scale distribution of matter such as galaxy distribution or cluster formation, but if we are interested in smaller details we have to add gas physics.    
There are two main approaches, completely different one from the other.    

<!--TEASER_END-->    

The first approach uses a grid to solve fluid equations. Fluid interactions are short range ones so we can use information from few nearby points to compute and evolve the quantities we are interested in at a point. Fluid must also respond to the gravitational field of the matter distribution. One can easily study shocks and discontinuities with this type of code.    
It is also possible to improve the resolution using mesh refinement but it's important to bear in mind that the resolution of mass particles and of hydrodynamics should be improved together. Grid codes can be expanded to include other effects such as magnetohydrodynamics.    
The second way is the Smoothed Particles Hydrodynamics (SPH). In these type of algorithms the fluid properties (pressure, density, temperature, ...) at any point can be found by averaging over particles in a region using a weight function. Because of this smoothing functions it has poor resolution of shocks and discontinuities and low resolution in low density regions. However these codes are quite easily to implement and has high resolution in high density regions.    
    
In both types of codes effects such as elementary chemical reactions, e.g. formation of hydrogen, molecules, cooling, heating, etc can be added because they are local effects. On the contrary star formation, feedback from stellar and other source, radiation transport, and so on are non-local and include a big range of scales so are difficult to implement.    
    
<em>References</em>:    
<ul>    
<li><a href="http://www.ias.ac.in/currsci/apr102005/1088.pdf" target="_blank" title="J.S. Bagla, Cosmological N-body simulation: Techniques, scope and status">J. S. Bagla, Cosmological N-body simulation: Techniques, scope and status</a></li>
<li><a href="http://adsabs.harvard.edu/abs/1991ComPh...5..164B" target="_blank" title="J.S. Bagla and T. Padmanabham, Cosmological N-body simulations">J.S. Bagla and T. Padmanabham, Cosmological N-body simulations</a></li>
</ul>
