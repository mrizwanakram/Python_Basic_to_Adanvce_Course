#Exception:  
#Exception are the errors detected while execution of program
#Exception are handled by try and except block
#print(10/0)   ZeroDivisionError
#print(10/'sdf')   TypeError

x = input("Enter a number: ")
y = input("Enter a number: ")
try:
    z = int(x) /  int(y)
except Exception as e:
    print("execution stopped due to error: ", e)
    z = None
print("Result: ", z)