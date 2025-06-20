def main():
    
    hello()
    names = input("What's your name? ")
    for name in names:
        print(f"{hello(name)}")
    

def hello(to ="World"):
    return f"hello, {to}"
    
if __name__=="__main__":
    main()