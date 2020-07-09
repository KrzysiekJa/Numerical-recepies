import numpy as np



def NewtonRaphson(fun1, fun2, dF1x, dF1y, dF2x, dF2y, x0, precision):
    iter_num = 0
    det, y2, y1, x2, x1 = 0.0, 0.0, 0.0, 0.0, 0.0
    jacobi_m = np.zeros((2,2))
    
    
    while(True):
        iter_num += 1
        
        det = (1/ (dF1x(x0[0])*dF2y(x0[1]) - dF1y(x0[1])*dF2x(x0[0])) )
        y2, y1, x2, x1 = dF2y(x0[0]), -dF1y(x0[0]), -dF2x(x0[1]), dF1x(x0[1])
        jacobi_m = np.array([[y2, y1], [x2, x1]])
        fun_vec  = np.array([fun1(x0[0], x0[1]), fun2(x0[0], x0[1])])
        
        x0  = x0 - det * np.matmul(jacobi_m, fun_vec)
        
        if(np.sqrt(np.sum(np.power(x0, 2))) < precision):
            break
    
    
    return x0, iter_num



if __name__ == "__main__":
    
    x1 = float(input("Provide start point first cordinate: "))
    x2 = float(input("Provide start point second cordinate: "))
    x0 = np.array([x1, x2])
    precision = float(input("Provide the precision: "))
    
    fun1 = lambda x, y: np.power(x, 3) + 2*np.power(y, 2)
    fun2 = lambda x, y: 4*x + np.sin(y)
    dF1x = lambda x: 3*np.power(x, 2)
    dF1y = lambda y: 4*y
    dF2x = lambda x: 4
    dF2y = lambda y: np.cos(y)
    
    result, iter_num = NewtonRaphson(fun1, fun2, dF1x, dF1y, dF2x, dF2y, x0, precision)
    
    print(fun1(result[0], result[1]), "for", result)
    print(fun2(result[0], result[1]), "for", result)
    print("after", iter_num, "itarations.")
    