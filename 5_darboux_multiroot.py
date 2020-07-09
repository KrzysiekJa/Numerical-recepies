import numpy as np


def bisection(function, a, b, precision):
    
    iter_num = 10
    interval = abs(a+b)/iter_num
    result= []
    new_a = 0.
    new_b = 0.
    mid   = 0.
    
    
    for i in range(iter_num):
        new_a = a + i * interval
        new_b = new_a + interval
        
        if(function(new_a) == 0):
            result.append(new_a)
            
        if(function(new_b) == 0):
            result.append(new_b)
            
        elif(function(new_a)*function(new_b) < 0):
            mid = (new_a + new_b)/2.
            while(abs(function(mid)) >= precision):
                mid = (new_a + new_b)/2.
                midFval = function(mid)
                
                if function(new_a)*midFval < 0:
                    new_b = mid
                elif function(new_b)*midFval < 0:
                    new_a = mid
                
            result.append(mid)
    
    return result



if __name__ == "__main__":
    
    precision  = float(input("Provide the precision: "))
    
    function = lambda x: np.cos(x)
    #function = lambda x: x**4 + x**3 - x**2 - 2*x - 2
    
    print(bisection(function, 0, 3 * np.pi, precision))
    