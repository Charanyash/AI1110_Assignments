import numpy as np
import pandas as pd
# Reading the frequency distribution table.
df = pd.read_excel("Freq_dist.xlsx")
# Converting the excel columns into numpy arrays.

# x --> Class mark vector 
x = df['marks'].to_numpy()

# freq --> frequency vector.
freq = df['Number of students(frequency)'].to_numpy()

a = np.ones(12)

mean = (freq@x)/(a@freq) # Vector approach.

print("The mean of scores is ",mean)
#x_repetition is intialised with zeros.
x_repitition = np.zeros(15)
count =0
# class marks are arranged w.r.t its frequency in x_repeition.
for i in range(0,len(freq)):
   for j in range(count,count+freq[i]):
         x_repitition[j] = x[i]

   count = count + freq[i]
#x_repetition contains scores of students in ascending order, median will be middle observation i.e., 8th obsevation.
median = x_repetition[8]
print("The value of median is ",median)
# from freq vector the max frequency is 3 which is corresponds to x[6] = 52.
mode = x[6]
print("The value of mode is ",mode)


         
        
         
