# Largest of three numbers
num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
num3 = int(input("Enter the third number:"))
if(num1>num2):
    if(num1>num3):
        print("First number i.e.",num1,"is largest")
    else:
        print("Third number i.e.",num3,"is largest")
elif(num2>num3):
    print("Second number i.e.",num2,"is largest")
else:
    print("Third number i.e.",num3,"is largest") 
            