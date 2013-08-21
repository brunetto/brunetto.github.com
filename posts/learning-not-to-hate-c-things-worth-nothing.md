<!-- 
.. link: 
.. description: 
.. tags: C, code, imported
.. date: 2012-05-21
.. title: Learning not to hate C: things worth nothing
.. slug: learning-not-to-hate-c-things-worth-nothing
-->


Here I would like to post some of the ideas, tricks, truths, and so on I've learned during the two-days course at the computing center. Two intense days of base C-programming full immersion, far beyond the flat and boring (and unuseful) orthodoxy you can find in a book.    

<!-- TEASER_END -->    

<strong>Header files</strong>    
They are one of the first annoying things I see in C/C++ languages. Two files for each "module", two lines to be modified every times, ... but I have eventually obtained a reasonable justification for their existence. When you distribute your code, or download someone's code, you can share or download compiled code+header files and not all the sources.    
    
<strong>Compile</strong>    
The easiest way to compile the sources and get the executable is    
    

````C    
gcc pippo.c -o pippo.x
````

where `pippo.c` is the source(s) (you can have `pippo1.c`, `pippo2.c` etc, but only one `main` function) file.    
A better way is to include some flags    
    

````C    
gcc -std=gnu99 -Wall -pedantic -Werror -O0 -g -o pippo.x pippo.c
````

where    

* `-std=gnu99` forces the compiler to the C99 standard (it includes some new features)
* `-Wall` to print all the compiler warnings
* `-pedantic` "Issue all the warnings demanded by strict ISO C and ISO C++; reject all programs that use forbidden extensions, and some other programs that do not follow ISO C and ISO C++" (from the `gcc` manual)
* `-Werror` transform the warnings into errors
* `-O0` no optimization
* `-g` produces debugging informations
* `-o` to specify the output

<strong>MACROS &amp; preprocessor</strong>    
    
The preprocessor is a sort of automated text editor. It cut and paste piece of text in the sources files according to some simple rules. With it you can define "constant" values or simple functions (danger, can lead to unpredicted effects) across the whole source and make easy to change it    

````C
#define PI 3.14
float a = PI;
````

but you can also check for already defined quantities, compile pieces of code ("conditional compilation") or implement a "header-guard" to avoid multiple imports of the same header    
    

````C    
#define CONDITION
#ifdef CONDITION
....
#else
....
#endif
````    

````C    
#ifndef HEADER_H
#define HEADER_H
.....
#endif
````

    
Compiling with the `-E` flag you can view the result of the preprocessor action.    
    
<strong>Numbers</strong>    
    
Number variables are similar to those in other programming languages, but there's some peculiarities.    
Integer dimension depends on the machine and on the compiler, on the contrary floats and doubles are fixed by an international standard. For the rest you can find detailed description on every C books.    
    
<strong>Cast</strong>    
    
It's possible to convert one type to some other type. For example,    
    

````C    
float pippo;
pippo = (float) k*1024L;
````

<strong>Bool</strong>    
    
There aren't boolean variables, but 0 stands for `False` and any other non-zero value means `True`.    
    
<strong>Side effect and short-circuit</strong>    
    
Something like    
    

````C    
i = k + 10 - ++k;
````

has indefinite result because it's not predictable the order of evaluation of operand/expression `k` and `++k`, and those expressions have <em>side effects</em> on the other expression involved in the result.    
Logical operators `&&` and `||` instead are evaluated strictly from left to right. This is c<em>alled short-circuit evaluation</em> and the operators are synchronization points, just like ";". At a synchronization point all the code before has to be already evaluated and the code after has not yet.    
    
<strong>Ternary operator</strong>    
    
The ternary operator accept three arguments and has the form of    
    

````C    
result = a &gt; b ? x : y;
````

This means `[expression_to_evaluate] ? [if true] : [if false]`. Obviously you can nest as many expression and operator as you want.    
    
<strong>Variables qualifiers</strong>    
    
In C there'are some qualifier that can be added to the type specification. Three of them are `const`, `extern` and `static`.    
The first can be added in the function declaration to tell the compiler that the values has not to be changed by the function, for example    

````C    
int pippo(const int pluto, const int* paperino);
````
means that the integer `pluto` and the pointer to integer `paperino` can not be changed by the function `pippo`.    
"extern" specifies that the variable is a global variable, coming from outside the function:    
    

````C    
int pippo;
int main(...){
	extern int pippo;
...
}
````

"static" has different meanings depending on where you put it.    
Before a global variable means that the variable is private of the file, and other files can not use it. Inside a function means that the variable survive after the end of the function (when the stack frame - the stack memory associated to the function - is deleted) and is available to the succeeding calls to the same function. Static is also used before a function to specify that the function is private of the file and can not be called outside:    
    

````C    
static int i;
static void foo(void){
	extern int i;
	static int j
}
````


* `i` is global inside the file but can not be called outside
* the function `foo` is private of the file and can not be called outside
* `j` survive after the termination of the function and maintains its value until the next call.

<strong>Pointers</strong>    
    
Pointers are special integer values that contains addresses of other values, for example:    
    

````C    
int i;
int* p;
p = &amp;i;
*p = 13;
````

first we define the integer `i`, then a pointer `p` to a integer value (here `*` means "the argument on the right is a pointer to a value of type defined by the argument on the left"), then we put the address of `i` in `p` (`&amp;` means "give me the address of the right argument") and at the end we modify the value of `i` dereferencing `p`, that is modifying the memory cell pointed by the address contained in p (here `*` means "follow the address contained in the argument on the right").    
It's possible to define pointers to pointers to pointers etc. adding "*". It exists the null pointer, that is an invalid pointer, and follow it result in a "segmentation fault" that means "you are trying to access memory you are not allowed to access". A pointer defined but not filled point to a random location in memory, so following it results in an indefinite result, probably a segmentation fault or the modification of another variable.     
Because the dereferencing operator has not the highest precedence, sometimes you will have to put parenthesis to specify the order of dereferencing:    
    

````C    
/*Filling a "heap" array using pointers*/
(*ptr)[i] = (float*) malloc(sizeof(float)*lenghtx);

/*In struct, the two forms are equivalent*/
(*pippo).pluto
pippo-&gt;pluto
````

<strong>Stack and heap</strong>    
    
The stack is the automatic memory used for the function calls, their local variables and the automatic arrays. It's managed automatically. The heap is the memory available to the user to define his variables. This has to be managed by the user so he has to deallocate the allocated memory and to keep track of the pointers (address). If you loose the pointer to some allocated memory this is lost until the end of the program and the memory can saturate. This is known as "<em>memory leak</em>".    
    
<strong>Arrays</strong>    
    
There'are basically two ways to create an array. First, you can create an automatic array in the stack memory, managed by the compiler. For this reason automatic arrays must be small and have to be defined at compile time, that means that you have to know and declare the dimension, for example;    
    
<pre>float array[10];</pre>
    
You can access the elements of the array in the natural way `array[3] = 10`.    
As a matter of fact, because an array it's a masked pointer, all of these are equivalent    
    

````C    
*V = 10;
V[0] = 10;
*(V+0) = 10;
0[V] = 10;
````

The operator "`[]`" is equivalent to dereferencing the address contained into the pointer on the left shifted by the quantity inside the operator, and to shift an address is equivalent to sum it to the shift because addresses are integer values and the memory occupied by an array is contiguous.    
    
The second type of array is defined by the user and manually allocated (and manually deallocated) in the heap memory with    
    

````C    
void* malloc(size_t size);
void free(void* heapBlockPointer);
````

In practice, the following is an example of how to implement two functions that create and destroy a two dimensional array given a pointer:    
    

````C    
#include 
#include 
#include "array_management.h"

/* Function definition, takes as argument the address of a pointer to pointer */
int array_creation(float*** ptr, int lenghtx, int lenghty){
	printf("Create array of pointers...n");

	/* In the memory cell of the pointer put the address of the first 
		element of an array of pointers to float and allocate the necessary space */
	*ptr = (float**) malloc(sizeof(float*)*lenghty); 

	/* Check that the allocation worked fine */
	if(*ptr==NULL){
	return -1;
	}
	printf("Create arrays...n");

	/* Allocate memory for an array of float for each pointer and put the address 
		of the first element in the respective cell of the array of pointers */
	for(int i=0; i&lt;lenghty; i++){
	(*ptr)[i] = (float*) malloc(sizeof(float)*lenghtx);
	if( (*ptr)[i] == NULL){
		return -1;
	}
	}
	return 0;
}

/* Function to deallocate the memory */
void array_destruction(float** ptr, int lenghty){
	printf("Destructing array...n");
	for(int i=0; i&lt;lenghty; i++){
	free(ptr[i]);
	}
	free(ptr); 
}
````
    
In both types of array there isn't a control on the indexes, it's up to the user not to read or write beyond the array limits.    
    
It's also important to keep in mind that arrays are contiguous memory blocks, and a multidimensional array is "linearized" row-major order so it's faster to "run" on the row index (that on the right-most one). This is known as <a href="http://en.wikipedia.org/wiki/Stride_of_an_array" target="_blank">stride one access</a>.    
    
<strong>Structs</strong>    
    
An array is a structure containing homogeneous data, if you need to put together different types of data you can use structs:    
    

````C    
struct point {
int x;
int y;}; /* Don't forget this semicolon!*/

struct point pippo;
pippo.x = 12;
pippo.y = 15;
````

It's also possible to use `typedef` to symplify the sintax:    

````C    
typedef struct treenode* Tree;
struct treenode {
int data;
Tree smaller, larger; /* equivalently, this line could say
};                       "struct treenode *smaller, *larger" */  
````

(From Cineca's slides)    
    
<strong>Strings</strong>    
    
Strings are simply arrays of characters, usually terminated with the "null" character "``" to be able to use the string manipulation libraries (without "``" you should give the length of the string to the library, but they are not designed to do this).    
Because of this, the two expression that follows are equivalent:    
    

````C    
void strcpy(char *s, char *t) {
	while ((*s = *t) != ‘’) {
	s++;
	t++;
	}
}
void strcpy(char s[], char *t) {
	/* s arr, t ptr */
	int i = 0;
	while ((*s = t[i]) != ‘’) {
	s++; /* s ptr */
	i++; /* t arr */
	}
}
````
    
(From Cineca's slides)    
    
<strong>Assignement evaluation</strong>    
    
Because the assignment operator "=" return the value assigned, it's possible to use this in expression evaluation to shorten the code, for example:    
````C    
void strcpy(char *s, char *t){while((*s++==*t++));}
````    
is equivalent to the expressions in the previous paragraph.