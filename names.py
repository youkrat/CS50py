name = input("What's your name? ")

# with as open("file.txt", "a(append)") as "variable name"
#automatically opens and closes a file
with open("names.txt", "a") as file:
    file.write(f"{name}\n")
    
#make sure to use file.close() when not using with 
