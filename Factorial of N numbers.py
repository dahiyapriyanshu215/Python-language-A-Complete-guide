N = int(input("Enter the number N:"))
fact = 1
for i in range(1,N+1,1):
    fact = fact * i
    i=i+1
print(fact)