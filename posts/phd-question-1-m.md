<!-- 
.. link: 
.. description: 
.. tags: astro/physics, cosmic_structure, Cosmology, PhD, imported
.. date: 2011-11-11
.. title: PhD question #1: M*
.. slug: phd-question-1-m
-->

In parallel with the series "Cosmological simulations" I'm starting now another series of posts about cosmology, astro/physics and related arguments. It may happen that your PhD advisor ask you a question about something and you are supposed to know the answer... but you don't! Or it may happen that you have to pass an admittance/qualification exam to enter your PhD student career on general astrophysical knowledge but you can't even remember some arguments exist! Because of these consideration and for my remembrance I will &nbsp;write down some of these questions and I will try to answer.<br />
<!-- TEASER_END --><br />
These posts don't pretend to be nor totally correct neither complete, but they reflect the answers I have found with, maybe, some corrections by other students or professors.<br />
<br />
So let's start with the first question: what is, how it is defined and how you can calculate $M_\*$.

$M_\*$ is the typical non-linear mass collapsing at the redshift we are considering. This means that $M_\*$ is the typical mass of a perturbation that, at the time we are looking, has the associated liner density contrast $\delta(\mathbf{x})\sim1$, or, in the formalism of the excursion set, pass the barrier of $\delta_c=1.686$.<br />
Starting from this and with the results of the linear theory we can obtain some qualitative laws for the non-linear evolution.<br />
From the linear theory we have that perturbations grow in a self-similar way ($\delta(\mathbf{x},t)=\delta(\mathbf{x})D(t)$, with $D(t)$ the growth factor) and, in an Einstein-de Sitter universe (a spatially flat universe containing only matter, the Friedmann universe in which the density exactly matches the critical one), the growth factor is proportional to the scale factor.<br />
Now, if we make a choice for the spectrum (scale-free spectrum), we can define the typical non-linear mass that is collapsing as<br />
$$M_\*(t)\propto D(t)^{6/(3+n)}$$<br />
that, in an Einstein-de Sitter universe, becomes<br />
$$M_\*(t)\propto a^{6/(3+n)}\propto (1+z)^{-6/(3+n)}$$<br />
where $n$ is the spectral index.<br />
From this we can derive other relations (still in the case of a EdS universe):<br />
<ul><br />
<li>$t_\*\propto (1+z)^{-3/2}$ the typical time of formation for a structure of mass $M_\*$</li>
<li>$\rho_\*\propto (1+z)^3$</li>
<li>$R\propto M_\*^{1/3}(1+z)^{-1}$</li>
<li>$\langle v\rangle^2M_\*^{2/3}(1+z)$</li>
</ul>
