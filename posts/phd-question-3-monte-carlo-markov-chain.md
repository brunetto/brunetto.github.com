<!-- 
.. link: 
.. description: 
.. tags: astro/physics, Computer, Cosmology, data_reduction, markov_chain, MCMC, PhD, imported
.. date: 2012-03-15
.. title: PhD question #3: Monte Carlo Markov chain
.. slug: phd-question-3-monte-carlo-markov-chain
-->

After <a href="http://www.brunettoziosi.eu/blog/wordpress/phd-question-1-latexm_latex/" target="_blank" title="PhD question #1: M*"></a> and <a href="http://www.brunettoziosi.eu/blog/wordpress/phd-question-2-spherical-collapse/" target="_blank" title="PhD question #2: spherical collapse"></a>, in thisp post I write about the Monte Carlo Markov chain. This post is the Wordpress transposition of a page in my private and local Mediawiki installation, so maybe has not a perfect structure and look&amp;feel. Also, the Latex formulas embedded in <a href="http://www.mediawiki.org/wiki/MediaWiki" target="_blank" title="Mediawiki homepage">Mediawiki</a> and <a href="http://wordpress.com/" target="_blank" title="Wordpress homepage">Wordpress</a> look horrible.    
Most of this post is made by paragraphs from <a href="http://en.wikipedia.org/wiki/Main_Page" target="_blank" title="Wikipedia homepage">Wikipedia</a> and from <a href="http://arxiv.org/abs/0712.3028" target="_blank" title="Licia Verde's article page">A practical guide to Basic Statistical Techniques for Data Analysis in Cosmology</a> by <a href="http://icc.ub.edu/~liciaverde/Home%20Page.html" target="_blank" title="Licia Verde homepage">Licia Verde</a> that I rearranged or try to explain and summarize.    
    
Essentially you can think a Markov chain as a set of states of physical system, or a series of values, depending on some parameters, in which every step/status depends only on the present status and not on the past. A Monte Carlo Markov chain is a Markov chain that proceeds trying random steps and tends to converge to an equilibrium that should be the best set of parameters we are looking for.    
To improve performances and precision usually more chains are used, starting from different and well-separated points, for a single estimation and a convergence criterion define when to stop.    
The steady state, or the equilibrium distribution, if it exists, roughly is the combination of parameters, o the vector for the probabilities to be in one status, that emerge to be constant in the long term. This means that if the system (the chain) at some time has a probability vector $q$ for the next status, it will have probability vector $q$ forever. $q$ is an eigenvector of the transition matrix with eingenvalue 1.    
    

<!-- TEASER_END -->    

    
<strong>Markov chain</strong>    
    
A Markov chain is a random process (sequence of random variables) that satisfy the Markov property. Usually the term "Markov chain" is used to mean a Markov process which has a discrete (finite or countable) state-space defined on a discrete set times.     
nevertheless "time" can take continuous values and the use of the term in Monte Carlo Markov Chain (MCMC) refers to cases where the process is defined on a discrete time-set (discrete algorithm steps) and a continuous state space.    
    
The Markov property states that the conditional probability distribution for the system at the next step (and in fact at all future steps) depends only on the current state of the system, and not additionally on the state of the system at previous steps.    
Formally, given a sequence of random variables $X_1, X_2, X_3, \dots$ we have    
    
$Pr(X_{n+1}=x|X_1=x_1, X_2=x_2, ldots, X_n=x_n) = Pr(X_{n+1}=x|X_n=x_n).,$    
    
The possible values$x_i$ of $X_i$ form a countable set $S$ called the <strong>state space</strong> of the chain.     
    
The changes of state of the system are called transitions, and the probabilities associated with various state-changes are called transition probabilities. The set of all states and transition probabilities for a given step form the <strong>transition matrix</strong> $p_{ij}$. The transition matrices completely characterizes a Markov chain.     
    
<strong>Types of chains</strong>    

* <strong>Time-homogeneous Markov chains</strong> (or <strong>stationary Markov chains</strong>) are processes where    $Pr(X_{n+1}=x|X_n=y) = Pr(X_n=x|X_{n-1}=y)$    for all $n$. The probability of the transition is independent of $n$.
* A <strong>Markov chain of order </strong> $m$ (or a Markov chain with memory&nbsp;$m$&nbsp;, where&nbsp;$m$&nbsp;is finite, is a process satisfying    $Pr(X_n=x_n|X_{n-1}=x_{n-1}, X_{n-2}=x_{n-2}, dots , X_1=x_1)$    that is    $Pr(X_n=x_n|X_{n-1}=x_{n-1}, X_{n-2}=x_{n-2}, dots, X_{n-m}=x_{n-m})text{ for }n &gt; m$    In other words, the future state depends on the past [latex]m[/latex] states.
* An <strong>additive Markov chain</strong>&nbsp;
* of order $m$ is a sequence of random variables $X_1, X_2, X_3, dots$, possessing the following property: the probability that a random variable $X_n$ has a certain value $x_n$ under the condition that the values of all previous variables are fixed depends on the values of $m$ previous variables only (Markov chain of order $m$), and the influence of previous variables on a generated one is additive,
* $Pr(X_n=x_n|X_{n-1}=x_{n-1}, X_{n-2}=x_{n-2}, \dots, X_{n-m}=x_{n-m}) = \sum_{r=1}^{m} f(x_n,x_{n-r},r)$.

<strong>Predictions</strong>    
    
    
Since the system changes randomly, it is generally impossible to predict with certainty the state of a Markov chain at a given point in the future. However, the statistical properties of the system's future can be predicted.    
The probability of going from state $i$ to state $j$ in $n$ time steps is    
$p_{ij}^{(n)} = Pr(X_n=j mid X_0=i) ,$    
and the single-step transition is    
$p_{ij} = Pr(X_1=jmid X_0=i). ,$    
For a time-homogeneous Markov chain:    
$p_{ij}^{(n)} = Pr(X_{k+n}=j mid X_{k}=i) ,$    
and    
$p_{ij} = Pr(X_{k+1}=j mid X_k=i). ,$    
The $n$-step transition probabilities satisfy the Chapman–Kolmogorov equation, that for any $k$ such that $0&lt;k&lt;n$,    
$p_{ij}^{(n)} = \sum_{r in S} p_{ir}^{(k)} p_{rj}^{(n-k)}$    
where $S$ is the state space of the Markov chain.    
The marginal distribution $Pr(X_n=x)$ is the distribution over states at time $n$. The initial distribution is $Pr(X_0=x)$. The evolution of the process through one time step is described by    
$ Pr(X_{n}=j) = \sum_{r in S} p_{rj} Pr(X_{n-1}=r) = sum_{r in S} p_{rj}^{(n)} Pr(X_0=r).$    
    
    
<strong>Example: a very simple weather model</strong>    
    
    
The probabilities of weather conditions (modeled as either rainy or sunny), given the weather on the preceding day,    
can be represented by a transition matrix:    
$P = \begin{bmatrix}0.9 &amp; 0.1 \ 0.5 &amp; 0.5\end{bmatrix}$    
The matrix $P$ represents the weather model in which a sunny day is 90%    
likely to be followed by another sunny day, and a rainy day is 50% likely to    
be followed by another rainy day. The columns can be labelled "sunny" and    
"rainy" respectively, and the rows can be labelled in the same order.    
$P_{ij}$ is the probability that, if a given day is of type $i$, it will be    
followed by a day of type $j$.    
Notice that the rows of $P$ sum to 1: this is because $P$ is a stochastic matrix.    

    
<strong>Predicting the weather</strong>    
    
    
The weather on day 0 is known to be sunny. This is represented by a vector in which the "sunny" entry is 100%, and the "rainy" entry is 0%:    
$ \mathbf{x}^{(0)} = \begin{bmatrix} 1 &amp; 0 \end{bmatrix}$    
The weather on day 1 can be predicted by:    
$ \mathbf{x}^{(1)} = \mathbf{x}^{(0)} P = \begin{bmatrix}1 &amp; 0 \end{bmatrix} \begin{bmatrix} 0.9 &amp; 0.1 .5 &amp; 0.5\end{bmatrix} = \begin{bmatrix} 0.9 &amp; 0.1 \end{bmatrix} $    
Thus, there is an 90% chance that day 1 will also be sunny.    
The weather on day 2 can be predicted in the same way:    
$ \mathbf{x}^{(2)} =\mathbf{x}^{(1)} P = \mathbf{x}^{(0)} P^2 = \begin{bmatrix} 1 &amp; 0 \end{bmatrix}\begin{bmatrix}0.9 &amp; 0.1 \ 0.5 &amp; 0.5 \end{bmatrix}^2= \begin{bmatrix} 0.86 &amp; 0.14\end{bmatrix} $    
or    
$ \mathbf{x}^{(2)} =\mathbf{x}^{(1)} P = \begin{bmatrix}0.9 &amp; 0.1\end{bmatrix} \begin{bmatrix}0.9 &amp; 0.1 .5 &amp; 0.5\end{bmatrix}= \begin{bmatrix} 0.86 &amp; 0.14 \end{bmatrix} $    
General rules for day $n$ are:    
$ \mathbf{x}^{(n)} = \mathbf{x}^{(n-1)} P $    
$ \mathbf{x}^{(n)} = \mathbf{x}^{(0)} P^n $    
<div>
    </div>
    
<strong>Steady state of the weather</strong>    
    
    
In this example, predictions for the weather on more distant days are increasingly    
inaccurate and tend towards a steady state vector. This vector represents    
the probabilities of sunny and rainy weather on all days, and is independent    
of the initial weather.    
The steady state vector is defined as:    
$ \mathbf{q} = \lim_{n \rightarrow \infty} \mathbf{x}^{(n)}$    
but only converges to a strictly positive vector if $P$ is a regular transition matrix (that is, there    
is at least one $P^n$ with all non-zero entries).    
Since the $q$ is independent from initial conditions, it must be unchanged when transformed by $P$. This makes it an eigenvector (with eigenvalue 1), and means it can be derived from $P$. For the weather example:    
$\begin{matrix} P & = & \begin{bmatrix} 0.9 & 0.1 \\ 
                                                        0.5 & 0.5 \end{bmatrix} \\ 
       \mathbf{q} P & = & \mathbf{q}  \mbox{(} \mathbf{q} \mbox{ is unchanged by } P \mbox{.)} \\ 
                            & = & \\mathbf{q}I \\ 
\mathbf{q} (P - I) & = & \mathbf{0} \\ 
                            & = &\\ 
\mathbf{q} \left( \begin{bmatrix} 0.9 & 0.1 \\ 
                                                  0.5 & 0.5 \end{bmatrix} - \begin{bmatrix} 1 & 0 \\ 
                                                     0 & 1 \end{\bmatrix} \right) \\ 
                             & = & \mathbf{q} \begin{bmatrix} -0.1 & 0.1 \ 0.5 & -0.5 \end{bmatrix} \end{matrix}$    
    
$ \begin{bmatrix} q_1 &amp; q_2 \end{bmatrix} \begin{bmatrix} -0.1 &amp; 0.1 \\ 0.5 &amp; -0.5 \end{bmatrix} = \begin{bmatrix} 0 &amp; 0 \end{bmatrix}$    
    
So    
$ -0.1 q_1 + 0.5 q_2 = 0$    
and since they are a probability vector we know that    
$q_1 + q_2 = 1.$    
    
Solving this pair of simultaneous equations gives the steady state distribution:    
$ \begin{bmatrix} q_1 &amp; q_2 \end{bmatrix} = \begin{bmatrix} 0.833 &amp; 0.167 \end{bmatrix}$    
In conclusion, in the long term, 83% of days are sunny.    
    
<strong>Monte Carlo Markov Chain (MCMC)</strong>    
    
Markov chain Monte Carlo (MCMC) methods (which include random walk Monte Carlo methods) are a class of algorithms for sampling from probability distributions based on constructing a Markov chain that has the desired distribution as its equilibrium distribution. The state of the chain after a large number of steps is then used as a sample of the desired distribution. The quality of the sample improves as a function of the number of steps.    
Usually it is not hard to construct a Markov chain with the desired properties. The more difficult problem is to determine how many steps are needed to converge to the stationary distribution within an acceptable error. A good chain will have rapid mixing—the stationary distribution is reached quickly starting from an arbitrary position—described further under Markov chain mixing time.    
Typical use of MCMC sampling can only approximate the target distribution, as there is always some residual effect of the starting position. More sophisticated MCMC-based algorithms such as coupling from the past can produce exact samples, at the cost of additional computation and an unbounded (though finite in expectation) running time.    
The most common application of these algorithms is numerically calculating multi-dimensional integrals. In these methods, an ensemble of "walkers" moves around randomly. At each point where the walker steps, the integrand value at that point is counted towards the integral. The walker then may make a number of tentative steps around the area, looking for a place with reasonably high contribution to the integral to move into next. Random walk methods are a kind of random simulation or Monte Carlo method. However, whereas the random samples of the integrand used in a conventional Monte Carlo integration are statistically independent, those used in MCMC are correlated. A Markov chain is constructed in such a way as to have the integrand as its equilibrium distribution. Surprisingly, this is often easy to do.    
    
<strong>Random walk algorithms</strong>    
Many Markov chain Monte Carlo methods move around the equilibrium distribution in relatively small steps, with no tendency for the steps to proceed in the same direction. These methods are easy to implement and analyze, but unfortunately it can take a long time for the walker to explore all of the space. The walker will often double back and cover ground already covered.  Here are some random walk MCMC methods:    

* Metropolis–Hastings algorithm: Generates a random walk using a proposal density and a method for rejecting proposed moves.
* Gibbs sampling: Requires that all the conditional distributions of the target distribution can be sampled exactly.  Popular partly because when this is so, the method does not require any 'tuning'.
* Slice sampling: Depends on the principle that one can sample from a distribution by sampling uniformly from the region under the plot of its density function.  This method alternates uniform sampling in the vertical direction with uniform sampling from the horizontal 'slice' defined by the current vertical position.
* Multiple-try Metropolis: A variation of the Metropolis–Hastings algorithm that allows multiple trials at each point. This allows the algorithm to generally take larger steps at each iteration, which helps combat problems intrinsic to large dimensional problems.

<strong>Avoiding random walks</strong>    
    
More sophisticated algorithms use some method of preventing the walker from doubling back. These algorithms may be harder to implement, but may exhibit faster convergence (i.e. fewer steps for an accurate result).    

* Successive over-relaxation: A Monte Carlo version of this technique can be seen as a variation on Gibbs sampling; it sometimes avoids random walks.
* Hybrid Monte Carlo (HMC): Tries to avoid random walk behaviour by introducing an auxiliary momentum vector and implementing Hamiltonian dynamics where the potential function is the target density.  The momentum samples are discarded after sampling.  The end result of Hybrid MCMC is that proposals move across the sample space in larger steps and are therefore less correlated and converge to the target distribution more rapidly.
* Some variations on slice sampling also avoid random walks.
* Langevin MCMC and other methods that rely on the gradient (and possibly second derivative) of the log posterior avoid random walks by making proposals that are more likely to be in the direction of higher probability density.

<strong>Monte Carlo Markov chain in Cosmology: CMB example</strong>    
    
In some cases, mapping the likelihood or the posterior distribution can be very time-expensive, so a MCMC can be used to investigate the likelihood space. The MCMC generates random draws (simulations) from the posterior distribution that are a “fair” sample of the likelihood surface. A properly derived and implemented MCMC draws from the joint posterior density    
$P(\alpha|x)$ once it has converged to the stationary distribution. The primary consideration in    
implementing MCMC is determining when the chain has converged. After an initial “burn-in” period, all further samples can be thought of as coming from the stationary distribution.    
In other words the chain has no dependence on the starting location.     
Another fundamental problem of inference from Markov chains is that there are always    
areas of the target distribution that have not been covered by a finite chain, it is thus crucial that the chain achieves    
good “mixing” so it can explore the support of the target distribution rapidly.    
It is important to have a convergence    
criterion and a mixing diagnostic. Plots of the sampled MCMC parameters or likelihood    
values versus iteration number are commonly used to provide such criteria. However, samples from a chain are typically serially correlated; very high auto-correlation leads to little movement of the chain and thus makes the chain to “appear” to    
have converged. Using a MCMC that has not fully    
explored the likelihood surface for determining cosmological parameters will yield wrong    
results.    
    
<strong>In practice</strong>    
    
Here are the necessary steps to run a simple MCMC for the CMB temperature power    
spectrum. It is straightforward to generalize these instructions to include the temperature-    
polarization power spectrum and other datasets. The MCMC is essentially a random walk in    
parameter space, where the probability of being at any position in the space is proportional    
to the posterior probability.    

1. Start with a set of cosmological parameters ${\alpha_1}$, compute the $Cl$ and the likelihood    $L_1 = L(Cl |Cl )$.
2. Take a random step in parameter space to obtain a new set of cosmological parameters    ${alpha_2 }$. The probability distribution of the step is taken to be Gaussian in each direction    i with r.m.s given by $\sigma_1$ . We will refer below to σi as the “step size”. The choice of    the step size is important to optimize the chain efficiency
3. Compute the $Cl$ for the new set of cosmological parameters and their likelihood $L_2$.    4.a) If $L_2 /L_1 \geq 1$, “take the step” i.e. save the new set of cosmological parameters ${\alpha_2}$    as part of the chain, then go to step 2 after the substitution ${\alpha_1 } \rightarrow {\alpha2 }$.    4.b) If $L_2 /L_1 &lt; 1$, draw a random number x from a uniform distribution from 0 to 1. If    $x \geq L_2 /L_1$ “do not take the step”, i.e. save the parameter set ${alpha_1 }$ as part of the    chain and return to step 2. If $x &lt; L_2 /L_1$, “ take the step”, i.e. do as in 4.a).
4. For each cosmological model run four chains starting at randomly chosen, well-    separated points in parameter space. When the convergence criterion is satisfied and    the chains have enough points to provide reasonable samples from the a posteriori    distributions (i.e. enough points to be able to reconstruct the 1- and 2-σ levels of the    marginalized likelihood for all the parameters) stop the chains.

    
<strong>Appendix</strong>    
    
<strong>Random process</strong>    
In probability theory, a stochastic process, or sometimes random process, is the counterpart to a deterministic process (or deterministic system). Instead of dealing with only one possible way the process might develop over time (as in the case, for example, of solutions of an ordinary differential equation), in a stochastic or random process there is some indeterminacy described by probability distributions. This means that even if the initial condition (or starting point) is known, there are many possibilities the process might go to, but some paths may be more probable and others less so.    
    
<strong>Bayesian statistic, likelihood, priori and posteriori distribution</strong>    
    
From http://www.thphys.uni-heidelberg.de/~amendola/statistics-ws2011.html, to be completed.    
We have a theory and some data, the Bayesian approach says that    
$P(T;D)=\frac{P(D;T)P(T)}{P(D)}$    
where:    

* $P(T;D)$ is the "conditional" probability of having the theory (theoretical parameters) given the data (that is the probability distribution of the parameters given the data observed and the prior knowledge on the parameters themselves) and it is called <strong>posterior distribution</strong> or sometimes likelihood
* $P(D;T)$ is the "conditional" probability of having the data given the theory and it is also called <strong>likelihood</strong>
* $P(T)$ is the probability of having the theory, that is the prior knowledge we have on the parameters, it's the <strong>prior distribution</strong>
* $P(D)$ is the probability of find the data, that is a normalization, it does not help in finding the parameters

The prior distribution is often unknown but can be of two kind: it can come from previous experiments or it can be the exclusion of some regions of the parameter space. The final result strongly depends on it.    
    
<strong>References</strong>    
    
* http://www.lorisbazzani.info/papers/old_projects/HMM_MPES.pdf
* http://www.dartmouth.edu/~chance/teaching_aids/books_articles/probability_book/book
* www.mathce.it/archivio/markov.pdf
* http://en.wikipedia.org/wiki/Markov_chain
* http://en.wikipedia.org/wiki/Stochastic_process
* http://www.vinz.info/catene-di-markov%3a-spam-che-piace-ai-motori-pt-1-4e1b78613a5d29b75200000a.html/li&gt;      
* http://www.thphys.uni-heidelberg.de/~amendola/statistics-ws2011.html
* http://arxiv.org/abs/0712.3028

