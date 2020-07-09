import numpy as np
from dill.source import getsource



def Euler(dy, x0, y0, xf, step):
    
    while(x0 <= xf):
        y0 += step * dy(x0, y0)
        x0 += step
    
    return x0, y0



def RudnyKutta2order(dy, x0, y0, xf, step):
    k1, k2 = 0, 0
    
    while(x0 <= xf):
        k1 =  dy(x0, y0)
        x0 += step
        k2 =  dy(x0, y0 + step*k1)
        y0 += step * 0.5 * (k1 + k2)
    
    return x0, y0



def RudnyKutta4order(dy, x0, y0, xf, step):
    k1, k2, k3, k4 = 0, 0, 0, 0
    
    while(x0 <= xf):
        k1 =  dy(x0, y0)
        k2 =  dy(x0 + 0.5*step, y0 + 0.5*step*k1)
        k3 =  dy(x0 + 0.5*step, y0 + 0.5*step*k2)
        x0 += step
        k4 =  dy(x0, y0 + step*k3)
        y0 += step * 1./6 * (k1 + 2*k2 + 2*k3 + k4)
    
    return x0, y0




if __name__ == "__main__":
    
    x0 = float(input("Provide beginning x value: "))
    y0 = float(input("Provide beginning y value: "))
    xf = float(input("Provide searching point value: "))
    step = float(input("Provide the computing step: "))
    print('Begining point: (', x0, ',', y0, ') with step of: ', step)
    
    dy = lambda x, y: np.power(x, 2) + y
    #dy = lambda x, y: 6 * np.power(y, 2) * x
    
    print('For equation: ', getsource(dy), '\nResults:')
    print( Euler(dy, x0, y0, xf, step), 'for Euler method')
    print( RudnyKutta2order(dy, x0, y0, xf, step), 'for Rugne-Kutta 2nd order method')
    print( RudnyKutta4order(dy, x0, y0, xf, step), 'for Rugne-Kutta 4th order method')
   