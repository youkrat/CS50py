#Defining the Hello function
def hello():
    print("Hello", end="", sep="")
#Removing whitespace and capitalizeing the user's name
name = input("What's your name? ",).strip().title()
first, second, surname = name.split()
#Calling the function hello, and saying hello to the user
hello()
print(f" {first}")
print(f"Is your full name, {first} {second} {surname}?")