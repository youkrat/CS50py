import sys 

try:
    print("Hello, my name is", sys.argv[1], sys.argv[2])
except IndexError:
    print("Add name")
