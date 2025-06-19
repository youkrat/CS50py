def main():
    
    while True:
        try:
            print("MODEL CALCULATOR")
            print("Select a function:")
            print("1. Square a number")
            print("2. Raise a number to a power")
            function=int(input("What function? "))
            
            if function==1:
                x= get_float("What's x:")
                print(f"{x} squared is, {square(x)}")
                
            elif function ==2:
                x=get_float("Enter base: ")
                y=get_float("Enter exponent: ")
                print(power(x,y))
            else:
                print("Unavailable, try again later")
        except ValueError:
            print("Please enter a valid number.")
        return
        
        

def square(n):
    return n * n
    
def power(a, b):
    return a**b
def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number")



if __name__ =="__main__":
    main()