import numpy as np

x = np.array([39.0,40.0,41.0,42.0,46.0,48.0,52.0,54.0,60.0,62.0,96.0,98.0])

freq = np.array([1,2,1,1,1,1,3,1,1,1,1,1])

a = np.ones(12)

mean = (freq@x)/(a@freq)

print("The mean of scores is ",mean)

x_repitition = np.zeros(15)
count =0

for i in range(0,len(freq)):
   for j in range(count,count+freq[i]):
         x_repitition[j] = x[i]

   count = count + freq[i]

print("The value of median is ",x_repitition[8])

print("The value of mode is ",x[6])
