import numpy as np
import pandas as pd


def gaussElimination(A, b):
    length = len(A)
    
    for i in range(length - 1):
        max_ind = abs(A[i:,i]).argmax() + i #argmax function is finding the bigggest value in axis
        
        if(A[max_ind, i] == 0):
            raise ValueError("Wrong matrix diagonal.")
        
        if max_ind != i:
            A[[i, max_ind]] = A[[max_ind, i]]
            b[[i, max_ind]] = b[[max_ind, i]]
        print(A, '\n')
        
        for j in range(i+1, length):
            multi = A[j][i]/A[i][i]
            A[j][i] = multi
            
            for k in range(i+1, length):
                A[j][k] = A[j][k] - multi * A[i][k]
                
            b[j] = b[j] - multi * b[i]
            print(A, '\n')
    
    result = np.zeros(length)
    i = length - 1
    result[i] = b[i]/A[i,i]
    
    while(i >= 0):
        result[i] = (b[i] - np.dot(A[i,i+1:], result[i+1:])) /A[i,i] #dot product
        i -= 1
    
    return result[:, np.newaxis]


if __name__ == "__main__":
    
    #!!! zmienić ścieżkę położenia pliku !!!
    df = pd.read_csv('3_gauss2.csv', index_col=None, header=None)
    b  = df.iloc[:,-1]
    A  = df.iloc[:, :-1].to_numpy()
    print(A, '\n\n', b, '\n')
    
    print (gaussElimination(A,b))