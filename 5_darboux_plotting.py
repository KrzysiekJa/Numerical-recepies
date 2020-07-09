import numpy as np
import matplotlib.pyplot as plt


def bisection(function, a, b, precision):
    
    if (function(a)*function(b) >= 0):
        raise ValueError("Wrong values of function in extremal points.")
    
    new_a = a
    new_b = b
    val_list = [(new_a, new_b)]
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
        val_list.append((new_a, new_b))
    
    
    x_val = np.linspace(a, b, 300)
    plt.plot(x_val, function(x_val), 'k-', linewidth=1.0, label='Właściwa funkcja')
    
    
    rColor = 1./len(val_list)
    red = 0
    for i in range(len(val_list)):
        plt.plot([val_list[i][0], val_list[i][1]], [function(val_list[i][0]), function(val_list[i][1])], color=(red, 0, 0), linewidth=0.5, label=str(i+1))
        plt.plot([val_list[i][0], val_list[i][1]], [function(val_list[i][0]), function(val_list[i][1])], 'o', color=(red, 0, 0), markersize=3)
        red += rColor
    
    
    plt.axhline(y=0, color="k", linewidth=0.5, linestyle="-")
    plt.legend(loc='lower left', ncol=2, numpoints=1, labelspacing=0.5, handletextpad=0.5, 
            handlelength=2.5, borderaxespad=0.5, borderpad=0.05, columnspacing=0.9, frameon=False)
    plt.show()
    
    return (new_a + new_b)/2.



if __name__ == "__main__":
    
    precision = 0.001
    
    function = lambda x: np.cos(x**3 - 2*x)
    #function = lambda x: x**2 - x - 1
    #function  = lambda x: np.log1p(x**2 + 2*x)
    
    print(bisection(function, -0.1, 2, precision))
    