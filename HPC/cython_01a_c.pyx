from random import random

cpdef double pi_montecarlo(int n=1000):
    
    cdef int n_in = 0, i
    cdef double x, y


    for i in range(n):
        x,y = random(), random()

        if x**2 + y**2 <= 1:
            n_in += 1
    return 4.0 * n_in / n