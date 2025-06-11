def add(a,b):
    result = a + b
    return result 
def square(n):
    return n*n
def divide(a,b):
    result= a/b
    return result
def operation():
    operation = int(input("What operation? "))
    if operation == 1:
             x=float(input("What is x? "))
             y=float(input("What is y? "))
             print(add(x,y))
    elif operation == 2:
        x=float(input("What number do you want to square? "))
        print(square(x))
    elif operation == 3:
        x=float(input("What is x? "))
        y=float(input("What is y? "))
        print(divide(x,y))
    else: 
        print("Outside current scope")
             
operation()