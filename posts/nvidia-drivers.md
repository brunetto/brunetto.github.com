<!-- 
.. link: 
.. description: 
.. tags: linux
.. date: 2013/08/19 10:17:08
.. title: Nvidia drivers
.. slug: nvidia-drivers
-->

If you need to install the NVIDIA drivers in your linux box yourcan encounter 
several problems.    
Here I try to summarize some useful step.

<!-- TEASER_END -->

First of all try to install the distribution packages, likely something like:    

* libcublas4                      - NVIDIA CUDA BLAS runtime library
* libcudart4                      - NVIDIA CUDA runtime library
* libcufft4                       - NVIDIA CUDA FFT runtime library
* libcurand4                      - NVIDIA CUDA Random Numbers Generation runt
* libcusparse4                    - NVIDIA CUDA Sparse Matrix runtime library 
* nvidia-common                   - Find obsolete NVIDIA drivers
* nvidia-compute-profiler         - NVIDIA Compute Visual Profiler
* nvidia-cuda-dev                 - NVIDIA CUDA development files
* nvidia-cuda-doc                 - NVIDIA CUDA and OpenCL documentation
* nvidia-cuda-gdb                 - NVIDIA CUDA GDB
* nvidia-cuda-toolkit             - NVIDIA CUDA toolkit
* nvidia-current                  - Transitional package for nvidia-current
* nvidia-current-updates          - Transitional package for nvidia-current-up
* nvidia-opencl-dev               - NVIDIA OpenCL development files
* nvidia-settings                 - Transitional package for nvidia-settings
* nvidia-settings-updates         - Transitional package for nvidia-settings-u     

If this fails, ty remove all the installed packages and driver and install that 
from the NVIDIA site:    

* Download the [NVIDIA drivers](http://www.nvidia.com/object/linux-display-amd64-310.40-driver.html)
and the [latest CUDA installers](https://developer.nvidia.com/cuda-downloads)

* stop the X server with    
```bash 
sudo service lightdm stop
```

* find them with     
````bash
aptitude search '~i' | grep "nvidia\|cuda\|libcu" | grep -v "kwin\|cups\|curl"
````
and check they are the installed packages and there are no other packages

* remove them with     
````bash
sudo aptitude --purge <packages names>
````

* blacklist all the modules that can interfere:    

1. in /etc/modprobe.d/blacklist.conf insert
````bash
blacklist amd76x_edac
blacklist vga16fb
blacklist nouveau
blacklist lbm-nouveau
blacklist rivafb
blacklist nvidiafb
blacklist rivatv
```

2. in /etc/modprobe.d/blacklist-nouveau.conf insert
````bash
blacklist nouveau
options nouveau modeset=0
blacklist lbm-nouveau
alias nouveau off
alias lbm-nouveau off
````

3. in /etc/default/grub insert
````bash
GRUB_CMDLINE_LINUX_DEFAULT="quiet splash nomodeset"
````

4. then run 
````bash
sudo update-grub
sudo update-initramfs -u
````

* see also [here](http://blog.bloemsaat.com/2013/03/17/installing-cuda-on-ubuntu-13-04-raring-ringtail/)

* install the drivers and then CUDA running the installers and following the 
instructions

* in /etc/modprobe.d/nvidia-installer-disable-nouveau.conf the NVIDIA installer should insert
````bash
blacklist nouveau
options nouveau modeset=0
````

* install some more libs
````bash
sudo apt-get install freeglut3-dev libxi-dev libxmu-dev
````

* reboot
