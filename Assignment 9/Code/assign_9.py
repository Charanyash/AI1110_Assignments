n = int(input("no. of observations:"))

m = int(input("No. of events in the partition:"))

X = float(input("enter the percentile of chi-square distribution:"))

print("enter the number of occurences of each event:")

lst=[]
for i in range(0,m):
    k = int(input())
    lst.append(k)

print("enter the theoritical probailities of each event:")
prob=[]
for i in range(0,m):
    p = float(input())
    prob.append(p)
    
q = 0

for i in range(0,m):
    q = q + (lst[i]-prob[i]*n)**2/n*prob[i]

print("The value of q(test statistic):",q)

if(q<X):
    print("The two events are independent")
