#Defining the Hello function and the parameters
#(to="world") sets the default value for the parameter to 
def hello(to="world"):
    print("Hello,", to )
#Calls hello without the name. Therefore; Hello world 
hello()
#Removing whitespace and capitalizing the user's name
name = input("What's your name? ",).strip().title()
first, second, surname = name.split()
#Calling the function hello, and saying hello to the user
hello(name)