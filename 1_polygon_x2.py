#Instruction:
#Program need python interpreter. For example in linux, please, use command: python3 1_polygon_x2.py
#in Windows use python 'idle' from programs.
#or: https://www.cs.bu.edu/courses/cs108/guides/runpython.html
#If necessery (needed numpy or matplotlib) use:
#pip install numpy
#pip install matplotlib
#
#If 'pip' is not present:
#https://pip.pypa.io/en/stable/installing/

import numpy as np
import matplotlib.pyplot as plt
plt.style.use('classic')


def lagrandeInterpolation(nodes, f_values, size, input):
    result = 0.0
    temp   = 1.0
    
    for i in range(0, size):
        for j in range(0, size):
            if(i == j):
                continue
                
            temp *= (input - nodes[j]) / (nodes[i] - nodes[j])
            
        result += temp * f_values[i]
        temp    = 1.0
        
    return result



x_val1 = [-2.0, -1.0, 1.0, 2.0]
x_val2 = [-4.0, -2.0, -1.0, 1.0, 2.0, 4.0]
x_val3 = [i/2.0 for i in range(-10, 11)]
x_val3.remove(0.0)

y_val1 = [1/(1+x*x) for x in x_val1]
y_val2 = [1/(1+x*x) for x in x_val2]
y_val3 = [1/(1+x*x) for x in x_val3]
print(y_val1, y_val2, y_val3)
y          = lambda x: 1/(1+x*x)
y_lagrange = lambda x,y,z,inp : lagrandeInterpolation(x, y, z, inp)
x_val = np.linspace(-5, 5, 300)



plt.plot(x_val, y(x_val), 'k-', linewidth=2.0, label='Właściwa funkcja')
plt.plot(x_val, y_lagrange(x_val1, y_val1, len(x_val1), x_val), 'b-', linewidth=0.8, label='Aproksymacja dla 4 punktów')
plt.plot(x_val, y_lagrange(x_val2, y_val2, len(x_val2), x_val), 'g-', linewidth=0.8, label='Aproksymacja dla 6 punktów')
plt.plot(x_val, y_lagrange(x_val3, y_val3, len(x_val3), x_val), 'r-', linewidth=0.8, label='Aproksymacja dla 20 punktów')
plt.plot(x_val1, y_val1, 'bo', markersize=9, label='4 punkty')
plt.plot(x_val2, y_val2, 'go', markersize=6, label='6 punkty')
plt.plot(x_val3, y_val3, 'ro', markersize=3, label='20 punktów')
plt.legend(loc='lower right', ncol=2, numpoints=1, labelspacing=0.5, handletextpad=0.5, handlelength=2.5, borderaxespad=0.5, borderpad=0.05, columnspacing=0.9, frameon=False)

plt.show()