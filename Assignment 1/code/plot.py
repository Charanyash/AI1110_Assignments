import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA
def line_gen(A,B):
    len =10
    dim = A.shape[0]
    x_AB = np.zeros((dim,len))
    lam_1 = np.linspace(0,1,len)
    for i in range(len):
        temp1 = A + lam_1[i]*(B-A)
        x_AB[:,i]= temp1.T
    return x_AB
# Collecting the points from a external file.
Points = np.loadtxt("data.txt")
A = Points[0]
B = Points[1]
C = Points[2]
D = Points[3]
B_r =Points[4]
C_r =Points[5]
D_r =Points[6]

#Generating lines
x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_CD = line_gen(C,D)
x_DD_r = line_gen(D,D_r)
x_D_rC_r = line_gen(D_r,C_r)
x_C_rB_r = line_gen(C_r,B_r)
x_B_rA = line_gen(B_r,A)

#Plotting the lines
plt.grid()


plt.plot(x_AB[0,:],x_AB[1,:],'k')
plt.plot(x_BC[0,:],x_BC[1,:],'k')
plt.plot(x_CD[0,:],x_CD[1,:],'k')
plt.plot(x_DD_r[0,:],x_DD_r[1,:],'k')
plt.plot(x_D_rC_r[0,:],x_D_rC_r[1,:],'k')
plt.plot(x_C_rB_r[0,:],x_C_rB_r[1,:],'k')
plt.plot(x_B_rA[0,:],x_B_rA[1,:],'k')

#Annotating the points.

plt.annotate("A",A,xytext=(0,5),textcoords="offset points")
plt.annotate("B",B,xytext=(0,5),textcoords="offset points")
plt.annotate("C",C,xytext=(0,5),textcoords="offset points",ha = 'right')
plt.annotate("D",D,xytext=(0,5),textcoords="offset points")
plt.annotate("B'",B_r,xytext=(0,5),textcoords="offset points")
plt.annotate("C'",C_r,xytext=(0,5),textcoords="offset points",ha = 'left')
plt.annotate("D'",D_r,xytext=(0,5),textcoords="offset points")
#scale and range for clear visibility.
plt.xlim([-4,4])
plt.ylim([-6,6])
plt.xticks(range(-4,4,1))
plt.yticks(range(-6,6,1))
plt.title('ARROW HEAD')
plt.savefig("../Figs/plot.png")
plt.show()
