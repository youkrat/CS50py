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
    
    y = get_int("What's x? ")
    print(f"x squared is {square(y)}")
    
main()
