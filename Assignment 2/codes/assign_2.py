import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA
from sympy import diff
from sympy.abc import x,y 


# Function f(x) defined here
def f(x):
    if (x<4):
        fval = 4 - x
        return fval
    else:
        fval = x - 4
        return fval

# Function f'(x) defined here.
def dif(x):
    if(x<4):
        fval = diff(4-y,y) # f'(x) is represented with variable y to avoid confusion. 
        return fval
    else:
        fval = diff(y-4,y)
        return fval


x = np.linspace(-2,10,1000)
fvec = np.vectorize(f)
difvec = np.vectorize(dif)
# Two figures are ploted to check continuity and differentiablity of f at x = 4.

plt.figure(1)
plt.plot(x,fvec(x),label='Function is continuous at x = 4')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid()
plt.savefig("../Figs/Figure_1")


plt.figure(2)
plt.plot(x,difvec(x),label='Function is not differentiable at x = 4')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid()
plt.savefig("../Figs/Figure_2")
plt.show()

