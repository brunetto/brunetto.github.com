<!-- 
.. link: 
.. description: 
.. tags: astro/physics, C, code, N-body, numerical, PhD, program, simulations, imported
.. date: 2012-02-20
.. title: Learning C from simulations, #3: C horrors!
.. slug: learning-c-from-simulations-3-c-horrors
-->


Yeah, this is post #3! Post #2 is "work in progress" and it will be on FFTs!    

Today I was trying to understand what this piece of code do:    

````c
for(i = 0; i < Nmesh / 2; i++)
    {
      for(j = 0; j < i; j++)
 seedtable[i * Nmesh + j] = 0x7fffffff * gsl_rng_uniform(random_generator);

      for(j = 0; j < i + 1; j++)
 seedtable[j * Nmesh + i] = 0x7fffffff * gsl_rng_uniform(random_generator);

      for(j = 0; j < i; j++)
 seedtable[(Nmesh - 1 - i) * Nmesh + j] = 0x7fffffff * gsl_rng_uniform(random_generator);

      for(j = 0; j < i + 1; j++)
 seedtable[(Nmesh - 1 - j) * Nmesh + i] = 0x7fffffff * gsl_rng_uniform(random_generator);

      for(j = 0; j < i; j++)
 seedtable[i * Nmesh + (Nmesh - 1 - j)] = 0x7fffffff * gsl_rng_uniform(random_generator);

      for(j = 0; j < i + 1; j++)
 seedtable[j * Nmesh + (Nmesh - 1 - i)] = 0x7fffffff * gsl_rng_uniform(random_generator);

      for(j = 0; j < i; j++)
 seedtable[(Nmesh - 1 - i) * Nmesh + (Nmesh - 1 - j)] = 0x7fffffff * gsl_rng_uniform(random_generator);

      for(j = 0; j < i + 1; j++)
 seedtable[(Nmesh - 1 - j) * Nmesh + (Nmesh - 1 - i)] = 0x7fffffff * gsl_rng_uniform(random_generator);
    }
````
    
<!-- TEASER_END -->    

It's a piece of the source of N-GenIC, Springel's ICs generator for <a href="http://www.gadgetcode.org/right.html" target="_blank" title="Gadget2">Gadget2</a>. Obviously no comments were present and I have no experience of how those codes work. I know that this is a way to fill the `seedtable` array, maybe a matrix that provides random seeds for the FFTs or to generate the [latex]delta[/latex]s for the realization of the density field. This array is stored in 1D so to access the elements we have to do some magic with indices. Trying to understand how the matrix is filled and how the indices works, and to practice with C I've wrote this piece of code:    
    

````c
#include <stdio.h>
#include <math.h>

int i = 0, j = 0;
int N = 10;

int main(int argc, char **argv){
  for(i = 0; i < N/2; i++){
    printf("i = %in", i);
    for(j = 0; j < i; j++)
      printf("t j= %in", j);
      if(!(i * N + j))
 printf("j doesn't existn");
      printf("tt i * Nmesh + j = %in",  i * N + j);
  /*
    a lot of commented code from the code above
  */
  }
  return 0;
}
````
    
    
The result was    
    

````bash
i = 0
j doesn't exist
                 i * Nmesh + j = 0
i = 1
         j= 0
                 i * Nmesh + j = 11
i = 2
         j= 0
         j= 1
                 i * Nmesh + j = 22
i = 3
         j= 0
         j= 1
         j= 2
                 i * Nmesh + j = 33
i = 4
         j= 0
         j= 1
         j= 2
         j= 3
                 i * Nmesh + j = 44
````
    
clearly wrong.    
So I've modified the code (thanks to my coworker) to print `j` and the expression in both the lines, and the result was    

````c
i = 0
j doesn't exist
         j= 0, i * Nmesh + j = 0
i = 1
         j= 0, i * Nmesh + j = 10
         j= 1, i * Nmesh + j = 11
i = 2
         j= 0, i * Nmesh + j = 20
         j= 1, i * Nmesh + j = 21
         j= 2, i * Nmesh + j = 22
i = 3
         j= 0, i * Nmesh + j = 30
         j= 1, i * Nmesh + j = 31
         j= 2, i * Nmesh + j = 32
         j= 3, i * Nmesh + j = 33
i = 4
         j= 0, i * Nmesh + j = 40
         j= 1, i * Nmesh + j = 41
         j= 2, i * Nmesh + j = 42
         j= 3, i * Nmesh + j = 43
         j= 4, i * Nmesh + j = 44
````
    
wrong again!    
    
The key is the second `for` statement, without the brackets. It was difficult to me to see this because C allows a for statement without brackets evaluating only the first line into the loop, and there were a lot of loop of one line commented into the code. The correct code    

````c
#include <stdio.h>
#include <math.h>

int i = 0, j = 0;
int N = 10;

int main(int argc, char **argv){
  for(i = 0; i < N/2; i++){
    printf("i = %in", i);
    for(j = 0; j < i; j++){
      printf("t j= %i, i * Nmesh + j = %in", j, i * N + j);
      if(!(i * N + j))
 printf("j doesn't existn");
      printf("t j= %i, i * Nmesh + j = %in", j, i * N + j);
  /*
    a lot of commented code from the code above
  */
    }
  }
  return 0;
}
````
    
works right!    
Obviously the Python version I've wrote before was perfect the first time I wrote it.!:P In Python, due to the mandatory indentation (and without those terrible brackets!:P) it's straightforward to understand what belong to a loop and what doesn't!


