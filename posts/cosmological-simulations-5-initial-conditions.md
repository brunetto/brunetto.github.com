<!-- 
.. link: 
.. description: 
.. tags: astro/physics, cosmic_structure, Cosmology, PhD
.. date: 2011-11-16
.. title: Cosmological simulations #5: initial conditions!
.. slug: cosmological-simulations-5-initial-conditions
-->

After we had a look on why we need cosmological simulations, what they are and how they are performed, it's time to learn more about the preparation of a simulation, in particular what are initial conditions and how we build them.    
<!-- TEASER_END -->
Usually, for a cosmological simulation, all the fields are linear so we can use linear theory to compute them. In linear theory the density contrast evolves as a combination of a growing and a decaying mode, but only the first survives, so we can set the initial system considering only the growing mode, and because until linearity is verified the density field and velocities are related to the gravitational potential we only need to generate the gravitational field and with it we can produce density and velocity fields.    
Once we have the initial potential there are two ways to generate the initial conditions:    

1. we can uniformly distribute the particles in the simulation box and choose the masses according to the gravitational field; velocities can be zero, in which case we increase the potential to account for the decaying mode, or non-zero and appropriate for the growing mode

2. we can displace uniformly distributed particles using the velocities of the linear theory; the displacement should be smaller than the interparticle separation or we can obtain a wrong power spectrum because a bigger displacement would lead the trajectories to cross and in this case, formally, the density contrast grows to infinite (this is not acceptable in linear approximation) and after that it decreases while the particles go away and this is not physical    


The relation that linking velocity and gravitational potential in the second entry:    
$\frac{\mathrm{d}\mathbf{v}}{\mathrm{d}t}+2\frac{\mathrm{d}a/\mathrm{d}t}{a}\mathbf{v}\propto \mathbf{g}=-\frac{\nabla\phi}{a}$
is the same both in linear theory and in the Zel'dovich approximation (this takes the non-linear equations together with the acceleration given by the linear theory to obtain results in the quasi-linear regime), so it's often said that the Zel'dovich approximation is used to set up initial conditions.    

Given that, the homogeneity of the initial unperturbed distribution it's very important because any inhomogeneity would combine with density perturbations modifying initial conditions. This homogeneity can be thought in different ways:

* a homogeneous but not random way is to put particles on a cubic grid but it could produce visible features due to the regular distribution
* we can consider putting particles at random positions but the $\sqrt{n}$ fluctuations will result in spurious clustering that will eventually dominate the fluctuations we want to simulate
* a good compromise could be placing particles in lattice cells with a random displacement from the center: this remove regularity but maintain uniformity
* the last possibility are "glass initial conditions" obtained by evolving an arbitrary distribution of particles in an n-body simulation with a repulsive force; it was invented by Simon White and the name refers to the molecular structure of glass, uniform but not regular    

Considering the last two possibilities, it's worth noting that the former still has a lot of noise, and the second is better than the grid only for aesthetic reasons.    

<strong>The initial gravitational potential</strong>

In standard cosmological models the initial perturbations density field is Gaussian. Since the linear evolution doesn't modify the statistics of density fields except for evolving the amplitude of perturbations, and because the potential and the density contrast are linked by a linear relation, the gravitational potential is also a Gaussian random field, and such a field is completely described in terms of the power spectrum of density perturbations. The Fourier components of a Gaussian random field (both real and imaginary part) are random numbers with a normal distribution and variance proportional to the power spectrum at that wave number. Also the phase of this random numbers has to be random, and changing it the resulting field is completely different.
We can generate the gravitational field in the Fourier space just using these properties and inverse transform it (or the force) to obtain the initial potential in real space. If we use adaptive mesh refinement codes we need Gaussian random fields with a variable resolution.    

<em>References</em>:

* <a href="http://www.ias.ac.in/currsci/apr102005/1088.pdf" target="_blank" title="J.S. Bagla, Cosmological N-body simulation: Techniques, scope and status">J. S. Bagla, Cosmological N-body simulation: Techniques, scope and status</a>
* <a href="http://adsabs.harvard.edu/abs/1991ComPh...5..164B" target="_blank" title="J.S. Bagla and T. Padmanabham, Cosmological N-body simulations">J.S. Bagla and T. Padmanabham, Cosmological N-body simulations</a>
