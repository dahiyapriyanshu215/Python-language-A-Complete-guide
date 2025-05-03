marks = {}
x = int(input("Enter marks for 'Physics' subject:"))
marks.update({'Physics':x})
y = int(input("Enter marks for 'Chemistry' subject:"))
marks.update({'Chemistry':y})
z = int(input("Enter marks for 'Maths' subject:"))
marks.update({'Maths':z})
print(marks)
print(type(marks))