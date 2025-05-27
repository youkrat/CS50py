#Asks user for their name, removes whitespace and capitalizes user's name
name = input("What's your name? ").strip().title()

#Splits user's name into first name last name and surname 
first, second, last = name.split(" ")
#Say hello to the user
print(f"Hello,{first} ",end="",sep=" ")
print (f"Is your full name,{first} {second} {last}?")