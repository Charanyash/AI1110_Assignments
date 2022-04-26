import numpy as np


# x --> Class mark vector, freq -> frequency vector.
x = np.array([39.0,40.0,41.0,42.0,46.0,48.0,52.0,54.0,60.0,62.0,96.0,98.0])
freq = np.array([1,2,1,1,1,1,3,1,1,1,1,1])
a = np.ones(12)

mean = (freq@x)/(a@freq) #Vector approach
print("The mean of scores is ",mean)
#x_repitition is intialied with zeros. 
x_repetition = np.zeros(15)
count =0
# class marks are arranged w.r.t its frequency in x_repetition.
for i in range(0,len(freq)):
   for j in range(count,count+freq[i]):
         x_repetition[j] = x[i]

   count = count + freq[i]
#x_repitition contains scores of students in ascending order , median will be middile observation i.e., 8 th obervation
median = x_repetition[7]
print("The value of median is ",median)
# from freq vector the max frequency is 3 which is corresponds to x[6]=52.
mode = x[6]
print("The value of mode is ",mode)
