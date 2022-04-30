import numpy as np
import pandas as pd
df = pd.read_excel("Freq_dist.xlsx")
x = df['marks'].to_numpy()
freq = df['Number of students(frequency)'].to_numpy()


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


         
        
         
