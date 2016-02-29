Thinning
========

This is a C implementation of Guo and Hall* thinning algorithm ported to Python 3. 

Thinning is the operation that takes a binary image and contracts the foreground until only single-pixel wide lines remain. 
It is also known as skeletonization.
This package implements the thinning algorithm by Guo and Hall* for Numpy arrays. 
It is thus compatible with OpenCV. The algorithm is implemented in C and fairly fast.

[*link](http://dx.doi.org/10.1145/62065.62074)
