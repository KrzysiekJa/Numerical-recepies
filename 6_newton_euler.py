import numpy as np


def NewtonMethod(function, derivative, start_p, precision):
    last_val = start_p
    iter_num = 0
    
    while(abs(function(start_p)) >= precision):
        iter_num += 1
        
        if(derivative(start_p) == 0):
            raise ZeroDivisionError
            
        start_p = start_p - function(start_p)/derivative(start_p)
        
        if(last_val - start_p):
            last_val = start_p
        else:
            start_p  = start_p + 0.0001
            last_val = start_p
            
    
    return start_p, iter_num


def EulerMethod(function, start_p, precision):
    iter_num = 0
    result = start_p
    next_p = start_p + 0.01
    
    while(abs(function(result)) >= precision):
        iter_num += 1
        
        result = next_p - ((next_p - start_p) * function(next_p)) / (function(next_p) - function(start_p))
        start_p = next_p
        next_p  = result
    
    
    return result, iter_num



if __name__ == "__main__":
    
    start_p   = float(input("Provide start point: "))
    precision = float(input("Provide the precision: "))
    
    function   = lambda x: x**3 - x**2 - 1
    derivative = lambda x: 3*x**2 - 2*x
    
    result = NewtonMethod(function, derivative, start_p, precision)
    
    
    print("x^3 - x^2 - 1 after ", result[1], " iterations with use of Newton method")
    print("x:", result[0], ", y:", function(result[0]))
    
    result = EulerMethod(function, start_p, precision)
    print("x^3 - x^2 - 1 after ", result[1], " iterations with use of Euler method")
    print("x:", result[0], ", y:", function(result[0]))