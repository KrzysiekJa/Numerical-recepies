import numpy as np


def bisection(function, a, b, precision):
    
    if (function(a)*function(b) >= 0):
        raise ValueError("Wrong values of function in extremal points.")
    
    new_a = a
    new_b = b
    mid   = (new_a + new_b)/2.
    
    while(abs(function(mid)) >= precision):
        mid = (new_a + new_b)/2.
        midFval = function(mid)
        
        if function(new_a)*midFval < 0:
            new_b = mid
        elif function(new_b)*midFval < 0:
            new_a = mid
        elif midFval == 0:
            return mid
        else :
            return None
    
    return (new_a + new_b)/2.



if __name__ == "__main__":
    
    precision  = float(input("Provide the precision: "))
    
    function = lambda x: np.cos(pow(x, 3) - 2*x)
    #function = lambda x: x**2 - x - 1
    #function  = lambda x: np.log1p(pow(x, 2) + 2*x)
    
    print(bisection(function, 0, 2, precision))