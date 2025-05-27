#Asks user for their name, removes whitespace and capitalizes user's name
name = input("What's your name? ").strip().title()

#Say hello to the user
print(f"Hello,{name} ",end="",sep=" ")
