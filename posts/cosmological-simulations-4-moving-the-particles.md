<!-- 
.. link: 
.. description: 
.. tags: 
.. date: 2011-11-13
.. title: Cosmological simulations: #4: Moving the particles!
.. slug: cosmological-simulations-4-moving-the-particles
-->

### Equations of motion

Once we have learned how to calculate gravitational forces and decided which way is best for us, it's time to move particles according to the force field.    
To have an idea of what happens we can look at a simplified version of the pp-method, where the new coordinates and velocities are expressed starting from the previous values:    

$\mathbf{v}_i^{new}=\mathbf{v}_i^{old}+\frac{\mathbf{F}_i}{m_i}\Delta t$
$\mathbf{x}_i^{new}=\mathbf{x}_i^{old}+\mathbf{v}_i\Delta t$

More in general we start from the Newtonian equation of motion for a set of particles interacting only through gravity, in particular we consider the Euler and Poisson equations. We express these in comoving coordinates because in this way we can focus on density and velocity perturbations, while the expansion of the universe is included in the scale factor $a$ (obtained from the Friedmann equations):    

$\frac{\mathrm{d}^2\mathbf{x}}{\mathrm{d}t^2}+2\frac{\mathrm{d}a/\mathrm{d}t}{a}\frac{\mathrm{d}\mathbf{x}}{\mathrm{d}t}=-\frac{1}{a^2}\nabla_x\phi$

$\nabla_x^2\phi=4\pi Ga^2\bar \rho\delta = \frac{3}{2}H_0^2\Omega_0\frac{\delta}{a}$

<!-- TEASER_END -->

Here $\mathbf{x}=\frac{\mathbf{r}}{a(t)}$ is the comoving coordinate of a particle, with $\mathbf{r}$ the physical coordinate; $\phi$ is the gravitational potential due to the density perturbations, $H_0$ the Hubble constant and $\Omega_0$ the density parameter at the present time. In real simulations these equations are modified changing variables to simplify the integration but the idea remain the same. They are valid for non-relativistic matter and on scales smaller than the Hubble radius $c/H_0$. The expansion of the universe act as a viscous force that opposes to the gravitational infall slowing down the growth of perturbations.    
Usually to integrate (read it as "to solve"!:P) the equations and obtain the new positions and velocities we use the Leap-Frog method because it minimizes the number of force evaluations. This is the most time consuming part of the code: Leap-Frog only requires one evaluation and the corresponding error is of the order of $\Delta t^3$. In this method positions and accelerations are computed at integer time steps and velocities at half time step: for example, positions are calculated at $t$ and velocities at $t+\Delta t/2$.    

### Time stepping

Choosing the simulation time step, that is the intervals between two calculation of positions and/or velocities, is crucial both for performances of the code and errors generation. Shorter time steps give smaller errors, but slow down the simulation.    
Time steps depend on the distribution of particles and may change during the evolution of the simulation. Use of individual time steps for each particle may speed up calculations, because we can tune the time step on for different particles, increasing the time resolution for particles in denser regions and decreasing it in low density regions. In this way larger $\Delta t$ are sufficient. When we decide the time step we have also to take care of the conservation of momentum and evolution of energy if it's not conserved (it can evolve according to the Irvine-Layzer equation).    
There are different possibility for how to calculate the time step, for example:    

*  we can take care of the validity of the Irvine-Layzer during the simulation; in this case we have to compute the force at mesh points and then interpolate it at particles positions but, because the force doesn't equal the gradient of the potential and the correction requires a direct sum on all the particles, this is not a good method
*  we can look at the convergence of velocities and final positions of particles using different time steps: reducing their duration we should approach the correct values
*  the reproducibility of initial conditions may be it's the most stringent criterion because it ensures that the results are correct: under certain conditions (linearity) running the particles forward and then back again we should get back the initial positions    

<em>References</em>:

* <a href="http://www.ias.ac.in/currsci/apr102005/1088.pdf" target="_blank" title="J.S. Bagla, Cosmological N-body simulation: Techniques, scope and status">J. S. Bagla, Cosmological N-body simulation: Techniques, scope and status</a>
* <a href="http://adsabs.harvard.edu/abs/1991ComPh...5..164B" target="_blank" title="J.S. Bagla and T. Padmanabham, Cosmological N-body simulations">J.S. Bagla and T. Padmanabham, Cosmological N-body simulations</a>

