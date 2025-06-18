import sys 

#Check for errors
if len(sys.argv)< 3:
    sys.exit("Too few arguments")
elif len(sys.argv)>3:
    sys.exit("Too many arguments")

#print name tags
print("Hello, my name is", sys.argv[1], sys.argv[2])
