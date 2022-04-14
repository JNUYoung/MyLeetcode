import numpy as np

def generateMatrix(n):
    """
        input : n 
        output : 2-dim array
    """
    origin_arr = [i+1 for i in range(n**2)]
    new_array = np.array([0]*n*n).reshape(n,n)
    
    


res = generateMatrix(3)
print(res)