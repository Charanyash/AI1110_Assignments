#Given that
students = 60

student_NCC = 30

student_NSS = 32

student_NCC_and_NSS = 24

# probability that students opted for NCC
prob_NCC = (float)(student_NCC)/(students)

# probability that students opted for NSS
prob_NSS = (float)(student_NSS)/(students)

# probability that students opted for both NCC and NSS
prob_NCC_and_NSS = (float)(student_NCC_and_NSS)/(students)

# Principle of inclusion and exclusion
prob_NCC_or_NSS = prob_NCC + prob_NSS - prob_NCC_and_NSS

print("The probability that the student opted for NCC or NSS :",prob_NCC_or_NSS)

# Demorgan's Law
prob_not_NCC_and_NSS = 1 - prob_NCC_or_NSS

print("The probability that the student has opted neither NCC nor NSS :",prob_not_NCC_and_NSS)

# Follows from the concept of probability of an event 
prob_NSS_but_not_NCC = prob_NSS - prob_NCC_and_NSS

print("The probability that the student has opted NSS but not NCC :",prob_NSS_but_not_NCC)
