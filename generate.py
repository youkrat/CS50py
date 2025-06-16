#Imports the randint module from random
from random import randint

#Gets a random number from 1-10
#Tests whether the number is even or odd and 
#prints heads for odd and tails for even
number = randint(1,10)
if number%2 != 0:
    print(f"{number} Heads")
else:
    print(f"{number} Tails")