# Largest of four numbers
num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
num3 = int(input("Enter the third number:"))
num4 = int(input("Enter the fourth number:"))
if(num1>num2):
    if(num1>num3):
        if(num1>num4):
            print("First number i.e.",num1,"is largest")
        else:
            print("Fourth number i.e.",num4,"is largest")   
    else:
        if(num3>num4):
            print("Third number i.e.",num3,"is largest")
        else:
            print("Fourth number i.e.",num4,"is largest")
else:
    if(num2>num3):
        if(num2>num4):
            print("Second number i.e.",num2,"is largest")
        else:
            print("Fourth number i.e.",num4,"is largest")    
    else:
        if(num3>num4):
            print("Third number i.e.",num3,"is largest")
        else:
            print("Fourth number i.e.",num4,"is largest")