def main():
    hello("World")
    goodbye("World")
    
def hello(name):
    print(f"Hello, {name}")
    
def goodbye(name):
    print(f"Goodbye, {name}")

#Only runs main when the file sayings.py is run and not any other file 
if __name__ == "__main__":
    main()