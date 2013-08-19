<!-- 
.. link: 
.. description: 
.. tags: astro/physics, Cosmology, domain decomposition, Gadget2, integrator, leapfrog, MPI, N-body, PhD, PM, simulation, springel, time-step, tree, TreePM, 
.. date: 2012-02-20
.. title: Cosmological simulations #9: Gadget-2 (N-body part)
.. slug: cosmological-simulations-9-gadget-2-n-body-part
-->

Here I would like to do a brief presentation of the main features of Gadget-2.    
Gadget-2 (<a href="http://www.mpa-garching.mpg.de/gadget/" target="_blank" title="Gadget2 homepage">here</a>, <a href="http://www.brunettoziosi.eu/blog/wordpress/my-first-gadget2-tests/" target="_blank" title="My first Gadget-2 tests">here</a> and <a href="http://onlinelibrary.wiley.com/doi/10.1111/j.1365-2966.2005.09655.x/abstract;jsessionid=DED86CDB5CD8A572F3631F0C42828086.d01t03" target="_blank" title="Gadget-2 paper">here</a>) is a cosmological simulation code developed primarily by <a href="http://www.mpa-garching.mpg.de/~volker/" target="_blank" title="Volker Springel's homepage">Volker Springel</a>. It is a <a href="http://www.brunettoziosi.eu/blog/wordpress/cosmological-simulations-3-calculating-the-force/" target="_blank" title="Cosmological simulations #3: force calculation!">TreePM</a> code so it splits forces between long-range (PM part) and short-range (tree part using multipole expansion to approximate the force of distant particles groups).    
    

<!-- TEASER_END-->    

    
<strong>The tree</strong>    
    
Gadget-2 uses a<a href="http://en.wikipedia.org/wiki/Octree" target="_blank" title="oct-tree"> BH oct-tree</a> (see also <a href="http://en.wikipedia.org/wiki/Barnes%E2%80%93Hut_simulation" target="_blank" title="Barnes&amp;Hut simulation on wikipedia">here</a>, <a href="http://www.artcompsci.org/~makino/softwares/C++tree/index.html" target="_blank" title="NBODY, an implementation of Barnes-Hut treecode">here</a>, <a href="http://ifa.hawaii.edu/~barnes/software.html" target="_blank" title="Barnes' page">here</a>, <a href="http://www.cita.utoronto.ca/~dubinski/treecode/treecode.html" target="_blank" title="A parallel tree code explenation">here</a> and <a href="http://www.prism.gatech.edu/~gth716h/BNtree/" target="_blank" title="Barnes-Hut Implementation in HTML/Javascript">here</a>) to calculate the short-range forces in the real space. This choice was done because this type of tree, compared to other types (KD-Tree, ...), requires the creation of less nodes, that imply that less memory is used. It's characterized by eight sub-nodes for each node and has only one particle in each leaf. The code decides to open a leaf according to a certain leaf opening criterion based on the estimated force error. The force for distant groups of particles is approximated with the multipole (here octopole) of the tree node and the error depends on the dimensions and the distances of the node considered.    
    
<strong>PM part</strong>    
    
The PM part of the code is used to calculate the long-range forces. The algorithm is something like:    
    
* CIC (cloud-in-cell) assignment is used to construct the mass density field on to the mesh from the information on the particles
    
* the discrete FT of the mesh is multiplied for the Green function for the potential in periodic boundaries (modified with the exponential truncation for the force splitting)
    
* deconvolution for the CIC kernel twice: the first for the smoothing effect of CIC assignment, the second for the force interpolation
    
* $\mathrm{FT}^{-1}$ to obtain the potential on the mesh
    
* finite differentiate the potential to obtain the forces
    
* interpolate the forces to the particles positions using CIC

    
Note: real-to-complex FT are used to save times and memory respect to full complex transforms.    
    
<strong>Time step</strong>    
    
This type of code has a large dynamic range in time scale, from the denser regions where the evolution is rapid to the less denser regions in which the evolution occur slower so we can describe it with larger time resolution. In this scenario evolving all particles with the smallest time-scale is a waste of time and computational resources. Because using different time-steps for each particle add instabilities to the system, Gadget-2 separates time-step between long-range (longer time step) and short-range (shorter time step) force computations. The perturbation of the system for different time-steps is related to the symplectic nature of the system, but I still have not understood what it really means and implies! I know that it refers to the phase space volume and has effect on the information conservation. May be in the future I'll write a post about this!    
Despite these arguments, sometimes individual time step are allowed because they perturb the system but not the symplecticity of the single particle.    
In the normal integration mode time-steps are discretized in a power of two hierarchy and particles can always move to smaller time steps but to longer time steps only in subsequent step, synchronized with higher time-steps. Alternatively the code can populate time-steps discretizeing them as integer multiples of the minimum time-step among the particles set. This lead to a more homogeneous distribution of particles across the time-line which can simplify work load balancing.    
The integration is performed using the <a href="http://en.wikipedia.org/wiki/Leapfrog_integration" target="_blank" title="Leapfrog method">leapfrog method</a>.    
    
<strong>Parallelization</strong>    
    
Usually the parallelization distributes particles across the CPUs using an orthogonal domain decomposition but in this way the trees built-in each domain depend on the domain geometry. Because the force depend on the tree (through the multipole expansion of the mass distribution) the force can be different if you change the number of processors.    
Gadget-2 introduce a space-filling fractal, the Peano-Hilber (PH) curve to map 3D space into a 1D curve that encompasses all the particles. Now the PH curve can be cut and each piece assigned to a CPU and in this way the force is independent of the processors number. If you cut every segment in eight pieces recursively you find again the tree decomposition, so there is a close correspondence between the decomposition obtained with the BH oct-tree and that of the PH curve.    
The PH curve has some remarkably properties, for example points that are close along the 1D PH curve are in general close in 3D space, so the mapping preserves locality and if we cut the PH curve into segments of a certain length we obtain a domain decomposition which has the property that the spatial domains are simply connected and quite "compact" (i.e., they tend to have small surface-to-volume ratios and low aspect ratio, a highly desirable property for reducing communication costs with neighbouring domains and for speeding up the local computation).    
    
<strong>Operations scheme</strong>    
Here a brief scheme on how the short range force calculation works on multiple processors. The PM computation uses the <a href="http://www.fftw.org/fftw2_doc/fftw_4.html" target="_blank" title="Parallel FFTWs">parallel FFTWs</a>.    
    
* Compute the PH key for each particle
    
* Sort the keys locally and split the PH curve into segments
    
* Adjust the sorted segments to a global sort, splitting and joining segments if needed, with little communication
    
* Assign the particles to the processes
    
* Construct a BH tree for the particles of each processors representing particles on other processors with pseudo-particles (acting like placeholders)
    
* During the tree traverse (e.g. in processor A) these pseudo-particles cannot be opened, the are flagged and inserted into a list that collects all the particles that are to be sent (=requested) to the other processors (e.g. to processor B)
    
* Processor B traverse again its local tree and send back the resulting force contribution to processor A

    
    
    
