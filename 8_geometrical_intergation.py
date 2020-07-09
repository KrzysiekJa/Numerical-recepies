import numpy as np
import matplotlib.pyplot as plt
from dill.source import getsource


def rectangleSum(fun, a, b, interv_num):
    #integration with use of midpoint
    dx = (b - a)/ interv_num
    midpoint = np.linspace(dx/2,b - dx/2,interv_num)
    
    result = np.sum(fun(midpoint) * dx)
    
    
    x_lin = np.linspace(a,b,interv_num+1)
    y_lin = fun(x_lin)
    
    X = np.linspace(a,b,interv_num*interv_num+1)
    Y = fun(X)
    plt.plot(X,Y,'b')
    x_mid = (x_lin[:-1] + x_lin[1:])/2
    y_mid = fun(x_mid)
    plt.plot(x_mid, y_mid,'b.', markersize=8)
    plt.bar(x_mid, y_mid, width=dx, alpha=0.3, edgecolor='b')
    plt.title('Intervals number = {}'.format(interv_num))
    plt.show()
    
    return result


def trapezoidSum(fun, a, b, interv_num):
    dx = (b - a)/ interv_num
    
    x_lin = np.linspace(a,b,interv_num+1)
    y_lin = fun(x_lin)
    y_right = y_lin[1:]
    y_left  = y_lin[:-1]
    
    result = 0.5 * dx * np.sum(y_right + y_left)
    
    
    X = np.linspace(a,b,interv_num*interv_num)
    Y = fun(X)
    plt.plot(X,Y)

    for i in range(interv_num):
        xs = [x_lin[i],x_lin[i],x_lin[i+1],x_lin[i+1]]
        ys = [0,fun(x_lin[i]),fun(x_lin[i+1]),0]
        plt.fill(xs,ys,'b',edgecolor='b',alpha=0.3)

    plt.title('Intervals number = {}'.format(interv_num))
    plt.show()
    
    return result




if __name__ == "__main__":
    
    a = float(input("Provide beginning value: "))
    b = float(input("Provide closing value: "))
    interv_num = int(input("Provide the precision: "))
    print('Interval: [', a, ',', b, '] with partition of: ', interv_num)
    
    #fun = lambda x: np.sin(x) + 1
    #fun = lambda x: np.sqrt(x)
    #fun = lambda x: np.exp(-x**2)
    fun = lambda x : 1/ (1 + x**2)
    
    print('For function: ', getsource(fun), '\nResults:')
    print( rectangleSum(fun, a, b, interv_num), 'for rectangles method')
    print( trapezoidSum(fun, a, b, interv_num), 'for tradezoids method')