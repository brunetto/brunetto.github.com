<!-- 
.. link: 
.. description: 
.. tags: astro/physics, Cosmology, N-body, PhD, simulation
.. date: 2011-11-02
.. title: Cosmological simulations #2: how?
.. slug: cosmological-simulations-2-how
-->

Let's try now to understand how simulations can be set up.<br />
<br />

First of all note that dark matter density dominates over ordinary (baryonic) matter at all times and we expect that ordinary matter follows the gravity of dark matter on large scales, so we can start considering only dark matter in our simulation.<br />
Moreover, cosmological simulations differ from other N-body simulations because they should to be able to manage comoving coordinates, i.e. coordinates that expand with the universe, since the universe is expanding.<br />

<!-- TEASER_END -->

In a cosmological simulation every particle represents a large number of dark matter particles, so the interaction between two particles represents the interaction between two "fluid elements", and this must be collisionless.<br />
Moreover, a point mass in the simulation represents a mass in a certain volume, and this volume change during the simulation due to the universe expansion and the clustering. This also imply that, at scales comparable to their physical size, they should feel less gravitational force than two point particles. When the two particles are separated by a distance comparable to the dimension of the fluid elements they represents, these would not feel the gravity of all the mass associated with the particles, as suggested by the Gauss theorem. This is because when you are into a spherical distribution of mass you only experience the gravitational force of the mass inside the radius corresponding to your distance from the center.<br />
To take care of this we decrease the strength of the force at small scales.<br />
Some example:<br />

<ul><br />
<li>GIF2: 6.6 kpc/h softening with a mean interparticle separation 110 Mpc/h / 400 particles = 275 kpc/h</li>
<br />
<li>Millennium: 5 kpc/h softening with a mean interparticle separation 500 Mpc/h / 2160 particles = 231 kpc/h</li>
<br />
<li>Millennium II: 1 kpc/h softening with a mean interparticle separation 100 Mpc/h / 2160 particles = 46 kpc/h</li>
</ul>

This is called "force softening". There are several ways to implement this and one should pay attention because a softening length smaller than the interparticle separation would lead to two-body relaxation problems. With the term "two-body relaxation" we mean the effects that arise when to particles mainly feels each other instead of feeling the global field, or feel more mass than what they should (they feel the mass of the entire fluid elements instead of the mass inside the radius corresponding to their distance). Usually the effects are of two types: the two particles can start to orbit faster and faster with decreasing separation, or they can experience a gravitational sling and be pulled apart (two-body scattering).<br />
The two-body relaxation modifies the density profiles of dark matter haloes (the dark matter structures formed by gravitational collapse of dark matter) making them smoother. The form of the softening is also important: historically there are two main softening, one is Gaussian and the other is a cubic spline.  <br />
<br />

Now we can start analyzing the structure of a cosmological N-body code. It consists in two main parts: the first computes the force field for a given configuration of particles, the second moves the particles according to the computed force field. The two modules are called at each step to ensure that the force field and the particles trajectories evolve in a self-consistent manner. Before starting the simulation we also need to set up the initial conditions and afterwards we have to write the output.<br />
<br />

In setting up our simulation there are some things we should consider.<br />
Our simulation represents a small box in the whole universe, but it isn't an isolated system so it feels the gravitational field of the rest of the universe. To take account of these we can set up periodic boundary conditions. This implies that space outside the simulation box is tiled it with copies (images) of the box. In this way particles near the edges are attracted not only by the matter in the box but also by the particles in its images.<br />
<br />
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><img alt="" height="500" src="http://isaacs.sourceforge.net/phys/images/these-seb/pbc-seb.png" style="margin-left: auto; margin-right: auto;" title="Periodic boundary conditions example" width="500" /></td></tr>
<tr><td class="tr-caption" style="text-align: center;"><span style="font-size: small; text-align: -webkit-auto;">Periodic boundary conditions example taken from <a href="http://isaacs.sourceforge.net/phys/pbc.html">http://isaacs.sourceforge.net/phys/pbc.html</a>.</span></td></tr>
</tbody></table>
<br />

With periodic boundary conditions one should make sure that there isn't a dominant object in its volume to avoid too large influence by its periodic copies.<br />
<br />

As written above, we need cosmological simulations to study scales where perturbations are not linear, to compare results with the real universe. To do this we must probe a large range of scales, so the mass of individual particles must be smaller than the mass of the smallest structure of interest. On the other hand the number of particles must be sufficient to cover the range of   masses involved in galaxy clustering. As of 2011 a typical large simulation have of order of billion of particles.<br />
<br />

With such large number of particles the most time consuming operation in the simulation is force calculation; therefore a number of algorithms  have been developed to avoid direct calculations, unfeasible even on the most powerful computer.<br />
<br />
<em>References</em>:<br />
<ul><br />
<li><a href="http://www.ias.ac.in/currsci/apr102005/1088.pdf" target="_blank" title="J.S. Bagla, Cosmological N-body simulation: Techniques, scope and status">J. S. Bagla, Cosmological N-body simulation: Techniques, scope and status</a></li>
<br />
<li><a href="http://adsabs.harvard.edu/abs/1991ComPh...5..164B" target="_blank" title="J.S. Bagla and T. Padmanabham, Cosmological N-body simulations">J.S. Bagla and T. Padmanabham, Cosmological N-body simulations</a></li>
</ul>
