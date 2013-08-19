<!-- 
.. link: 
.. description: 
.. tags: astro/physics, code, Computer, Cosmology, N-body, PhD, simulation, imported
.. date: 2012-04-03
.. title: PhD question #4: calculate the value of M*
.. slug: phd-question-4-calculate-the-value-of-m
-->

Some post ago [I've written about M*](phd-question-1-m.html), the typical non-linear mass collapsing at the redshift we are considering. Now I have to find a value for it.     

<!-- TEASER_END -->    

I said that $M^*$ is the typical mass of a perturbation that, at the time we are looking, has the associated liner density contrast $\delta(\mathbf{x})\sim1$, or, in the formalism of the excursion set, pass the barrier of &nbsp;$\delta_c=1.686$.     
This means that we are looking for a perturbation with $\sigma\simeq1.686$ and trying to quantify the mass it contains.    
    
<strong>$\sigma$ and R</strong>    
    
First of all we need to find the radius of a perturbation whose $\sigma$ reached the value of 1.686. To do this we can use the <a href="http://www.brunettoziosi.eu/blog/wordpress/the-initial-conditions-saga/" target="_blank" title="The “Initial Conditions” saga">code</a> developed to manage the CAMB files in order to find the matter power spectrum and its normalization. Then we add few lines to "sample" the$\sigma(R)$ distribution and find the radius of the perturbation reaching the excursion set barrier for the collapse.     
    
<strong>$M^*$</strong>    
    
Once we have the radius for which $\sigma = \delta_c$ we need to know the mean density in the universe to find $M^*$ with:    
    
$M^* = \frac{4}{3}\pi R_*^3\rho_m$    
    
<del>I don't know why we only need to use $\rho_m$ and not $\rho_m\delta$ or something similar is not clear to me, but it's correct.</del>We use this formula because $M^*$ is a quantity related to the linear perturbations. It's correct because the difference between a linear and a non-linear perturbation is the value of the density contrast, but the mass is the same. In other words, the mass of a perturbation is the same both in the linear and in the non-linear evolution, but linear perturbations have smaller density contrasts and larger radii, non-linear perturbations instead have larger density contrasts and smaller radii. To be precise, the previous equation can be written:    
$M^* = \frac{4}{3}\pi R_*^3\rho_{bg}(1+1.686) = \frac{4}{3}\pi R_{vir}^3\rho_{bg}(1+200)$.    
To obtain $\rho_m$ we find the value of the critical density $\rho_c$ and multiply it for $\Omega = \rho_m / \rho_c$. These two values can be obtained from books (<a href="http://www.amazon.com/Cosmology-Prof-Peter-Coles/dp/0471489093/ref=ntt_at_ep_dpt_2" target="_blank" title="Coles &amp; Lucchin">Lucchin</a>, <a href="http://www.amazon.com/Galaxy-Formation-Evolution-Houjun-Mo/dp/0521857937/ref=sr_1_1?s=books&amp;ie=UTF8&amp;qid=1333458377&amp;sr=1-1" target="_blank" title="Mo, van den Bosch &amp; White">Mo&amp;White</a> for example) or in the <a href="http://lambda.gsfc.nasa.gov/product/map/dr2/params/lcdm_wmap.cfm" target="_blank" title="WMAP data page">WMAP data page</a>. In the second case we prefer to use the single data fit because it's simpler to refer to it.    
    
Here's the code:    
    
````python
#!/use/bin/env python
import time
import numpy as np
import matplotlib.pyplot as plt
import random as rnd
from scipy import integrate

""" Calculate M* . M* is propto the mass contained in the radius for which 
s_8=delta_c refer to: 
http://www.brunettoziosi.eu/blog/wordpress/the-initial-conditions-saga/
http://www.brunettoziosi.eu/blog/wordpress/phd-question-3-calculate-the-value-of-m/
"""

t = time.time()

#===============================================================================
#    Compute sigma
#===============================================================================

### Load data from the nasa-CAMB file 

# matterpower is the file with the k and the total matter spectrum
# transfer is the file with the k and the transfer function for the various 
#species, the 6th column is for the total matter (baryons+DM)
transfer = np.genfromtxt('camb_88704620_transfer_out_z0.dat', usecols = (0,6))
#matterpower = np.genfromtxt('2012-01-30_data/camb_88704620_matterpower_z0.dat')

# CAMB CDM transfer output
camb_k = transfer[:,0]
camb_tf = transfer[:,1] 

R = 8 #Mpc/h
s_8 = 0.9#0.8118405 #from WMAP7 but we need the values for the Millennium-2, so 
# we use its s_8
sp_ind = 1
delta_c = 1.686

### Calculate the amplitude to normalize the spectrum:
### P(k) = Ak^nT^2(k) 

# FT of the window function (spherical top-hat)
def FTW(R, k): 
	""" Return the Fourier transform of the window function 
	(spherical top-hat)
	"""
	return 3.*(np.sin(k*R)-k*R*np.cos(k*R)) / (k*R)**3

def spectrum():
	"""Calculate the power spectrum given the transfer function and the FT of the window 
	function.
	"""
	# camb_k**(2+sp_ind) that is k^(2+n) because d^3k=4pi k^2dk
	amp_integrand = camb_k**(2+sp_ind)*camb_tf**2 * FTW(R, camb_k)**2
	amp_integral = integrate.trapz(amp_integrand, camb_k)
	# Amplitude for s_8 = 1
	amp_0 = 2*np.pi**2/amp_integral
	# Amplitude
	amp = amp_0*s_8**2  # 9.9197881817e-09
	#print amp
	# Calculate the power spectrum
	return camb_k**sp_ind*camb_tf**2 * amp

# Calculate the power spectrum
ps = spectrum()

# Calculate sigma on the radii
def sigma(R):
	"""Return the sigma for the current radius.
	"""
	return pow(integrate.trapz(camb_k**2 * ps * FTW(R, camb_k)**2, camb_k)/(2*np.pi**2), 0.5)

#===============================================================================
#    Find the radius containing M*
#===============================================================================

# Initialize some variables
neigh = np.ones(2) # two nearest neighbours sigmas
r_min = 10**(-2) # min r to sample
r_max = 10**2 # max r ti sample
i = 0 # loop counter

# While stops when the computed sigma is less then 0.001 from delta_c
while np.abs(np.amin(delta_c+neigh)) &gt; 0.001:
print "Loop ", i
i+=1
print "Condition start ", np.abs(np.amin(delta_c+neigh))
# radii to be sampled
r = np.linspace(r_min, r_max, num=100)
# Compute sigma for those radii, the minus sign is to avoid resorting of the
# array to be used by np.searchsorted
s_r = -np.asarray(map(sigma, r))
# Find the two nearest neighbours
neigh[0] = np.amax(s_r[s_r  -delta_c])
# Find the corresponding radii
r_min = r[np.searchsorted(s_r, neigh).min()]
r_max = r[np.searchsorted(s_r, neigh).max()]
print "Sigmas", -neigh[0], -neigh[1]
print "Radii [Mpc/h] ", r_min, r_max
print "Condition end ", np.abs(np.amin(delta_c+neigh))

# Selected values
s_star = neigh[np.argmin(delta_c+neigh)]
r_star = r[np.searchsorted(s_r, s_star)]
deviation = np.abs(np.amin(delta_c+neigh))

print "############################################"

print "Selected sigma ", -s_star
print "Selected radius [Mpc/h] ", r_star

print "Calculate M* using:"
print "Gt4.299 x 10^(-9) Mpc /M_sun (km/s)^2tfrom Mo&amp;White"
print "Ht100*h^2"
print "Omega_mt0.25tfrom the Millennium-2 simulation"
print "Omega_mt0.241tfrom WMAP7"

#===============================================================================
#    Cosmological parameters and find the mean density in the Universe
#===============================================================================

H = 100
h = 0.732 #WMAP http://lambda.gsfc.nasa.gov/product/map/dr2/params/lcdm_wmap.cfm
G = 4.299*10**(-9)
omega_m_mill = 0.25
omega_m_WMAP = 0.241

# Until here it's correct
rho_c = 3*H**2/(8*np.pi*G) # 2.7766040316101764 * h**2 x 10^11 M_sun/Mpc^3
	# 2.778 from Lucchin book
	# 2.775 from Mo&amp;White book

rho_mean_mill = rho_c * omega_m_mill # 6.94151007903 * h**2 x 10^10 M_sun/Mpc^3 = 3.71942769658 x 10^10 M_sun/Mpc^3
	rho_mean_WMAP = rho_c * omega_m_WMAP # 6.69161571618 * h**2 x 10^10 M_sun/Mpc^3 = 3.58552829951 x 10^10 M_sun/Mpc^3

print "rho_c = 3H^2/8 pi G = ", rho_c," h^2 M_sun/Mpc^3"
print "Millennium-2 rho_mean = omega_m_mill * rho_c = ", rho_mean_mill, " h^2 M_sun/Mpc^3 = ", rho_mean_mill*h**2
print "WMAP7 rho_mean = omega_m_WMAP * rho_c = ", rho_mean_WMAP, " h^2 M_sun/Mpc^3 = ", rho_mean_WMAP*h**2 

#===============================================================================
#    Compute M*
#===============================================================================

M_star_mill = np.pi * r_star**3 * rho_mean_mill * 4./3#* (delta_c + 1)
M_star_WMAP = np.pi * r_star**3 * rho_mean_WMAP * 4./3#* (delta_c + 1)

print "M* Millennium-2 ", M_star_mill, " M_sun/h" # 4.81467115575e+12 M_sun/h
print "M* WMAP ", M_star_WMAP, " M_sun/h" # 4.64134299414e+12 M_sun/h

#===============================================================================
#    Compare with Hayashi&amp;White 2008 article
#===============================================================================

print "Hayashi&amp;White's value:"

M_star_white = 6.15*10**(12)
omega_m_white = 3.*M_star_white/(4*np.pi*r_star**3*rho_c)

print "M*: ", M_star_white
print "Omega_m", omega_m_white

r_s = pow(3.*M_star_white/(4*np.pi*rho_mean_mill), 1./3)
s_white = sigma(r_s)

print "As alternative:"
print "R* ", r_s
print "Sigma ", s_white

#===============================================================================
#    Summary
#===============================================================================

print ""
print "##############################################################################################################"
print "SUMMARY"
print "##############################################################################################################"
print ""
print "WhottttM*ttR*ttOmegattSigmattSigma-delta_c"
print "--------------------------------------------------------------------------------------------------------------"
print "Hayashi&amp;White given Rtt{:e}t{:e}t{:e}t{:e}t{:e}".format(M_star_white,r_star,omega_m_white,-s_star,deviation)
print "Hayashi&amp;White given Omegat{:e}t{:e}t{:e}t{:e}t{:e}".format(M_star_white,r_s,omega_m_mill,s_white,np.abs(s_white-delta_c))
print 'Me WMAP datattt{:e}t{:e}t{:e}t{:e}t{:e}'.format(M_star_WMAP,r_star,omega_m_WMAP,-s_star,deviation)
print "Me Millennium-2 datatt{:e}t{:e}t{:e}t{:e}t{:e}".format(M_star_mill,r_star,omega_m_mill,-s_star,deviation)
print ""
print "##############################################################################################################"
print "##############################################################################################################"
print ""
print "Done in ", time.time()-t
````
	
The differences between the different values of $M^*$ are acceptable and probably depends on different integration boundaries for $\sigma$.