import sys 

#Check for errors
if len(sys.argv)< 3:
    sys.exit("Too few arguments")
#Skips the first element of the list(name.py)
for arg in sys.argv[1:]:
    print("Hello, my name is", arg)
