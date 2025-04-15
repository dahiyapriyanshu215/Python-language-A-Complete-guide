num = int(input("Enter the number:"))
if(num<=6):
    print("Wrong choice")
else:        
    if(num%7==0):
        print("It is a multiple of 7")
    else:
        print("It is not a multiple of 7")