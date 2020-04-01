# Program to multiply two matrices using nested loops
import random
import numpy as np

def generate_matrix(N):
    # NxN matrix
    X = np.empty([N,N])
    X = np.random.randint(100, size=(N, N))
    
    # Nx(N+1) matrix
    Y = np.empty([N,N])
    Y = np.random.randint(100, size=(N, N))

    return (X, Y)

def empty_results():
    # result is Nx(N+1)
    result = np.zeros([N, (N+1)])
    return result

def insert_results(result):
    result=np.matmul(X, Y)
    return(result)
                
                
def show_results():
    for r in result:
        print(r)

N = 250
(X, Y) = generate_matrix(N)
result=empty_results()
result=insert_results(result)
show_results()