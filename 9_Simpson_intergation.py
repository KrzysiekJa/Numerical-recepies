import numpy as np
from dill.source import getsource



def SimpsonMethod(fun, a, b, interv_num):
    if interv_num %2 == 1:
        raise ValueError("Number of intervals must be an even integer.")
    
    dx = (b - a)/ interv_num
    x  = np.linspace(a, b, interv_num+1)
    y  = fun(x)
    
    result = (dx/3) * np.sum(y[0:-1:2] + 4*y[1::2] + y[2::2])
    
    return result


def MonteCarlo(fun, a, b, interv_num):
    dx = (b - a)/ interv_num
    x  = np.array(np.random.uniform(a, a + dx, 4))
    
    for i in range(interv_num-1):
        a = a + dx
        x = np.vstack([x, np.random.uniform(a, a + dx, 4)])
    
    y = fun(x)
    
    result = np.sum(dx * np.mean(y, axis=1))
    
    return result



def quadratureMethod2(fun, a, b, interv_num):
    tFun = lambda a,b : [(b+a)/2 + ((b-a)/2) * (-np.sqrt(3)/3), 
                         (b+a)/2 + ((b-a)/2) * (np.sqrt(3)/3)]
    dx   = (b - a)/ interv_num
    result = 0
    
    for i in range(interv_num):
        t = tFun(a, a + dx)
        a = a + dx
        result += (dx/2) * (fun(t[0]) + fun(t[1]))
    
    return result


def quadratureMethod4(fun, a, b, interv_num):
    result = 0
    dx   = (b - a)/interv_num
    tFun = lambda a,b: np.array([(b+a)/2 + ((b-a)/2) *(-(1/35) * np.sqrt(525 + 70 * np.sqrt(30))), 
                  (b+a)/2 + ((b-a)/2) *(-(1/35) * np.sqrt(525 - 70 * np.sqrt(30))),
                  (b+a)/2 + ((b-a)/2) *((1/35) * np.sqrt(525 + 70 * np.sqrt(30))), 
                  (b+a)/2 + ((b-a)/2) *((1/35) * np.sqrt(525 - 70 * np.sqrt(30)))])
    A = np.array([(1/36) * (18-np.sqrt(30)), (1/36) * (18+np.sqrt(30)),
                  (1/36) * (18+np.sqrt(30)), (1/36) * (18-np.sqrt(30))])
    
    x = np.linspace(a, b, interv_num+1)
    t = np.array([tFun(x[i], x[i+1]) for i in range(interv_num)])
    y = fun(t)
    
    result = np.sum((dx/2) * (A[0] * y[:,0] + A[1] * y[:,1] + A[2] * y[:,2] + A[3] * y[:,3]))
    
    return result




if __name__ == "__main__":
    
    a = float(input("Provide beginning value: "))
    b = float(input("Provide closing value: "))
    interv_num = int(input("Provide the precision: "))
    print('Interval: [', a, ',', b, '] with partition of: ', interv_num)
    
    fun = lambda x: np.power(x, 3) + 2
    #fun = lambda x: np.sqrt(x)
    #fun = lambda x: np.exp(-x**2)
    #fun = lambda x : 1/ (1 + x**2)
    
    print('For function: ', getsource(fun), '\nResults:')
    print( SimpsonMethod(fun, a, b, interv_num), 'for Simpson method')
    print( MonteCarlo(fun, a, b, interv_num), 'for Monte Carlo method')
    print( quadratureMethod2(fun, a, b, interv_num), 'for quadrature method with 2 nodes')
    print( quadratureMethod4(fun, a, b, interv_num), 'for quadrature method with 4 nodes')