import math
import random
import numpy as np
import matplotlib.pyplot as plt

N = 100000
M = 0

XCirculo=[]  
YCirculo=[]  
XQuadrado=[]  
YQuadrado=[] 

for p in range(N):
    x=random.random()
    y=random.random()

    if(x**2+y**2 <= 1):
        M+=1
        XCirculo.append(x)  
        YCirculo.append(y)        
    else:
        XQuadrado.append(x)  
        YQuadrado.append(y)

Pi = 4*M/N
print('N=%d M=%d Pi=%.2f' %(N,M,Pi))


X=np.linspace(0,1)
Y=[]
for x in X:
    Y.append(math.sqrt(1-x**2))

plt.axis   ("equal")                             
plt.grid   (which="major")                        
plt.plot   (X , Y, color="red" , linewidth="4") 
plt.scatter(XCirculo, YCirculo, color="red", marker   =".") 
plt.scatter(XQuadrado, YQuadrado, color="yellow"  , marker   =".") 
plt.suptitle  ("Monte Carlo method for Pi estimation")
 
plt.show()
