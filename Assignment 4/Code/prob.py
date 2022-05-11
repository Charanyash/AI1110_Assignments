import numpy as np
import pandas as pd

df = pd.read_excel("data.xlsx")
count = df['Count'].to_numpy()

student_NCC = count[0]
student_NSS = count[1]
student_NCC_and_NSS = count[2]
N = count[3]# Sample Size

#Theoritical Probabilities.

# probability that students opted for NCC
prob_NCC = (float)(student_NCC)/N

# probability that students opted for NSS
prob_NSS = (float)(student_NSS)/N

# probability that students opted for both NCC and NSS
prob_NCC_and_NSS = (float)(student_NCC_and_NSS)/N

# Principle of inclusion and exclusion
prob_NCC_or_NSS = prob_NCC + prob_NSS - prob_NCC_and_NSS

print("The theoritical probability that the student opted for NCC or NSS :",prob_NCC_or_NSS)

# Demorgan's Law
prob_not_NCC_and_NSS = 1 - prob_NCC_or_NSS

print("The theoritical probability that the student has opted neither NCC nor NSS :",prob_not_NCC_and_NSS)

# Follows from the concept of probability of an event 
prob_NSS_but_not_NCC = prob_NSS - prob_NCC_and_NSS

print("The theoritical probability that the student has opted NSS but not NCC :",prob_NSS_but_not_NCC)

#Experimental probabilities.
x = np.random.randint(0,2,size =(N,2))# Each array represents [X=x,Y=y] where X,Y are random variables.

c_NCC = np.array([i for i in x if i[0] == 1])#opted for NCC

c_NSS = np.array([i for i in x if i[1] == 1])#opted for NSS

c_NCC_and_NSS = np.array([i for i in x if i[0] == 1 and i[1] == 1])# opted for NCC and NSS.

pr_NCC = (float)(len(NCC))/N

pr_NSS = (float)(len(NSS))/N

pr_NCC_and_NSS  =  (float)(len(NCC_and_NSS))/N

pr_NCC_or_NSS = pr_NCC + pr_NSS - pr_NCC_and_NSS

print("The experimental probability that the student opted for NCC or NSS :",pr_NCC_or_NSS)

pr_not_NCC_and_NSS = 1 - pr_NCC_or_NSS

print("The experimental probability that the student opted neither NCC nor NSS :",pr_not_NCC_and_NSS)

pr_NSS_not_NCC = pr_NSS - pr_NCC_and_NSS

print("The experimental probability that the student has opted NSS but not NCC :",pr_NSS_not_NCC)

