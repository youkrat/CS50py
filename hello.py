#Defined get_int with the parameter prompt
#Displays desired message when prompting for an int 
def get_int(prompt):
    while True:
        try:
            x =float(input(prompt))
        except ValueError:
            pass
        else:
            return x
def square(n):
    return n*n

def main():
    #Changed the prompting from get_int() to main():
    # In case of additional functions e.g addition
    y = get_int("What's x? ")
    print(f"x squared is {square(y)}")
    
main()
