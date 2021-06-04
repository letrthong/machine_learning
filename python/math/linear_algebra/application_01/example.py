#sudo apt-get install python-numpy python-scipy
import numpy as np
import scipy.linalg as la
import scipy as sp

#pip install matplotlib
#sudo apt-get install python-tk
# importing the required module 
import matplotlib.pyplot as plt 

P = np.array([[6, 5, 3, 1], 
    [3, 6, 2, 2],
    [3, 4, 3, 2]])

Q  =  np.array([[1.50, 1,00],
        [2.00, 2.50],
        [5.00, 4.50],
        [16.00, 17.0]])

print(P)
print("")
print(Q)
print("")
#R = np.dot(P, Q)
R = P.dot(Q) 
print(R)