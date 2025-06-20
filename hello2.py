def main():
    
    hello()
    name = input("What's your name? ").strip().title()
    hello(name)
 

def hello(to ="World"):
    print("Hello,",to)
    
if __name__=="__main__":
    main()