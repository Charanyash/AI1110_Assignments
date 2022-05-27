import math
from math import sqrt
import numpy as np
import matplotlib.pyplot as plt

def F_x(x):
     if((x>=-2)and(x<=2)):
         return (x+2)/4.0
     if(x>2):
            return 1
     else : return 0

def F_y(y):
    if(y>=0 and y<=4):
        return sqrt(y)/2.0
    if(y<0):
        return 0
    else : return 1

def f_y(y):
    if(y>=0 and y<=4):
        return 1/((4.0)*sqrt(y))
    
x = np.linspace(-4,4,100)

y = np.linspace(-8,8,100)

plt.figure(1)
plt.plot(x,list(map(F_x,x)))
plt.xlabel('x')
plt.ylabel('Probability Distribution of x')

plt.figure(2)
plt.plot(y,list(map(F_y,y)))
plt.xlabel('y')
plt.ylabel('Probability Distribution of y')

plt.figure(3)
plt.plot(y,list(map(f_y,y)))
plt.xlabel('y')
plt.ylabel('Probability Density function of y')
         
plt.show()
