import numpy as np
import pandas as pd


def jacobiMethod(A, b, precision, iterations):
    length = len(A)
    weak   = False
    
    for i in range(length - 1):
        
        if(2*np.absolute(A[i,i]) - np.sum(np.absolute(A[i,:])) < 0):
            raise ValueError("Not diagonally dominant matrix.")
        
        if(2*np.absolute(A[i,i]) - np.sum(np.absolute(A[i,:])) > 0):
            weak = True
    
    if(weak == False):
        raise ValueError("Not diagonally weakly dominant matrix.")
    
    
    x0 = np.zeros((length, 1))
    D  = np.diag(np.diag(A))
    LU = np.tril(A) + np.triu(A) - 2*D
    D  = np.linalg.inv(D)
    print(x0,'\n', D,'\n', LU, '\n\n')
    
    
    for i in range(iterations):
        
        result = - np.matmul(np.matmul(D,LU), x0) + np.matmul(D, b)
        
        if(np.sqrt(np.sum(np.power(x0 - result, 2))) < precision):
            iterations = i
            break
        if(i + 1 < iterations):
            x0 = result
    
    
    print(precision, np.sqrt(np.sum(np.power(x0 - result, 2))), "Iterations :", iterations)
    
    return result



if __name__ == "__main__":
    
    precision  = float(input("Provide the precision: "))
    iterations = int(input("Provide the ny,ber of iterations: "))
    
    #!!! zmienić ścieżkę położenia pliku !!!
    df = pd.read_csv('4_jacobi.csv', index_col=None, header=None, delimiter=' ')
    b  = df.iloc[:,-1].to_numpy()
    b  = b[:, np.newaxis]
    A  = df.iloc[:, :-1].to_numpy()
    print(A, '\n\n', b, '\n')
    
    print('\n', jacobiMethod(A, b, precision, int(iterations)))