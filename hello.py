def get_int():
    while True:
        try:
            x =float(input("What is x? "))
        except ValueError:
            pass
        else:
            return x
def square(n):
    return n*n

def main():
    
    y = get_int()
    print(f"x squared is {square(y)}")
    
main()
