<!-- 
.. link: 
.. description: 
.. tags: astro/physics, cosmic_structure, Cosmology, PhD, imported
.. date: 2011-11-13
.. title: Cosmological simulations #3: force calculation!
.. slug: cosmological-simulations-3-force-calculation
-->

In the previous posts we wrote about cosmological simulations, why we need them, how they are performed and which are the important things to care about.
Now we are ready to learn the algorithms developed to compute gravitational forces between the particles.    

<!-- TEASER_END -->

### Direct summation: PP method

The raw approach is to calculate forces between all pairs in the simulation. This works well for less than $10^3$. The number of pairs, and therefore the computational time, scales as $N^2$, so this method that is usually unacceptable given the number of particles in a simulation.    
It's difficult to implement periodic boundary conditions in this method (because you have to manage it by hand) and the only convenient way to do this is to use the Ewald summation.    
This method is mostly used to test other methods.    

### Tree method

The disadvantage of the pp-method comes from having to compute the interaction of any new particle with all the others. The tree method, on the contrary, approximate the force of a distant group of particles with the force exerted by only one particle, in the center of mass of the group, with mass equal the total mass of the group. In this way the computation scales as $N\log N$.    
To create the groups the particles are divided and arranged in a tree structure, that is, the initial volume is divided, and every resulting volume divided again. This procedure goes on until in the resulting volumes there's only one particle. In this situation it's very important the "cell acceptance criterion" that decide whether or not a cell is far enough to be used as it is or if it has to be divided into its subvolumes.    
The accuracy and the speed of this method can be improved storing some information about the particles in the volumes (such as moments of the mass distribution, usually the quadrupole).    
Moreover, close particles can share information about distant groups because the force is very similar, and the tree can be parallelized efficiently. However, it's not so easy to consider periodic boundary conditions.    

### Fast multipole method

This method is an improved version of the tree method. It is based on including higher moments of the mass distribution in cells and some other optimizations. This method has a computational costs which scales as $N$.    

However all these method has problems with the open boundary conditions and it's difficult to adapt it to the cosmological needs. An extension of the tree method with explicit momentum conservation has been also developed.    

### Particle-mesh method

This is the first method used extensively for cosmological simulations and the first used for simulation with order of $10^5$ particles. The PM method solve the Poisson equation (partial differential equation that links the gravitational field with the mass distribution) in the Fourier space, where it is a simple algebraic equation, using the FFT (Fast Fourier Transform) routine to change from coordinate space to the Fourier space and viceversa&nbsp;. FFT requires to sample the functions at uniformly spaced points and here we use a grid (mesh). We compute density at the grid points using weight functions on the particles representing the density and velocity fields.    
The use of Fourier methods automatically include periodic boundary conditions without no additional effort (because of the nature of periodic function in the Fourier space) and the use of the mesh automatically soften the force at small scales (because of the interpolation needed to compute the gravitational field on the grid) but it underestimate the force at scales larger (toughly up to 3 times) than the softening length.    
This method is parallelized using parallel FFT and dividing the volume among the processors.    
Softening at the mesh scale give collisionless evolution but the code cannot resolve structure at scales smaller than the mesh scale, moreover the mesh makes the force anisotropic at small scales. This happens because the grid points don't sample very well the filed on such small scales.    

### Adaptive-mesh refinement

In AMR methods the mesh is refined in high density regions using a finer grid, but it's important to pay attention to the conservation of momentum and angular momentum switching from a grid to another.    

### P3M: particle-particle+particle-mesh

The idea is to add a correction to the force calculated with the PM method by using the PP method on the closest particles. The correction is assumed to be isotropic and depend only upon the distance. Usually it's considered a distance of the order of 2 times the internode mesh distance. This method has been parallelized but with some problems, also because load balancing is quite difficult to achieve.

Some other problems are:    

* the correction to the force is isotropic but the PM method has anisotropies at small scales
* the correction is at scales up to 2 times the grid scale but the PM method underestimate the force on scales larger than these
* the refined interparticle softening is at scales smaller than the interparticle separation and this can lead to two-body scattering and relaxation
* P3M simulations slow down at late times when the distribution of particles becomes highly clustered because the short range force dominate the compute operations    

### Tree+PM: TPM

Some hybrid codes has been developed trying to combine the PM and the Tree methods:    

* The Grid of Trees PM (GOTPM)replaces the PP part of P3M with a local tree in each region. This resolve only the last problem of the P3M.
* TPM correct the short range force only if the particle is in a highly dense region and with a tree to compute the forces.
* TreePM divide the force in long-range and short-range instead of correcting the PM force at a certain scale, greater than that of the P3M. The short-range forces are calculated with a global tree.
* The Adaptive TreePM (ATreePM) try to resolve the two-body relaxation and scattering using an adaptive softening length, determined by the local density. To ensure momentum conservation force is simmetrized for particles closer than the softening length. The softening correspond to consider the particles with a density profile and not only mass points and if the softening length is different for two close particles, the force they feel is different between them. This happens &nbsp;because particle A feel a force due to its entire mass and a certain fraction of particle B mass, but particle B feels a force due to its own mass and a different fraction of the mass of particle A. In this case the forces are symmetrized taking the mean of the two forces.

To compare different methods we can consider:    

* The dynamic range, that is the range of scales over which the force is computed reliably. Usually the limit is at small scales rather than at large scales.
* The code should integrate the equation of motion in a reproducible way and momentum should be conserved.
* The code should be efficient and run with the minimum possible time
* Requirement of memory and other resources.

<em>References</em>:

* <a href="http://www.ias.ac.in/currsci/apr102005/1088.pdf" target="_blank" title="J.S. Bagla, Cosmological N-body simulation: Techniques, scope and status">J. S. Bagla, Cosmological N-body simulation: Techniques, scope and status</a>
* <a href="http://adsabs.harvard.edu/abs/1991ComPh...5..164B" target="_blank" title="J.S. Bagla and T. Padmanabham, Cosmological N-body simulations">J.S. Bagla and T. Padmanabham, Cosmological N-body simulations</a>

