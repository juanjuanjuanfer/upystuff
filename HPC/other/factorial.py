import numpy as np
def fact_i(n):
    '''
    Fucntion to obtain factorial of n by iteration.
    '''
    result = 1
    for i in range(1,n+1):
        result = result * i
    return result

def fact_r(n):
    '''
    Function to obtain factorial of n by recurssion.
    '''
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact_r(n-1)
        
def exp_i(x, n):
    '''
    Function to estimate exp(x) via Taylor Series aprroximation considering n terms.
    '''
    exp = 1 
    for i in range(1,n+1):
        exp += x ** i / fact_i(i)
    return exp

def exp_r(x,n):
    '''
        Function to estimate exp(x) via Taylor Series aprroximation considering n terms.
    '''
    exp = 1
    for i in range(1,n+1):
        exp += x ** i / fact_r(i)
    return exp

def exp_o(x,n):
    '''
            Function to estimate exp(x) via Taylor Series aprroximation considering n terms.
    '''
    exp = 1
    factorial = 1
    for i in range(1, n+1):
        factorial *=i
        exp += x ** i / (factorial)
    return exp

def benchmark():
    exp_i(50,100)
    exp_r(50,100)
    exp_o(50,100)

if __name__ == '__main__':
    benchmark()
