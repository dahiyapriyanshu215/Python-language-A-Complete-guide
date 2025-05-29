N = int(input("Enter the limiting number N:"))
i = 1
fact = 1
while i<=N:
    fact = fact * i
    i=i+1
print("Factorial upto",N,"natural numbers is:",fact)