#sudo apt-get install python-numpy python-scipy
import numpy as np
import scipy.linalg as la
import scipy as sp

#pip install matplotlib
#sudo apt-get install python-tk
# importing the required module 
import matplotlib.pyplot as plt 

a = np.array([1,3,-2,1])
print(a)

t = sp.linspace(0, 1, 100)
plt.plot(t, t**2)
plt.show()