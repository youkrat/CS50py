#Added a type hint to let the program know that n should be an int
#-> str hints that the return value of meow should be str
def meow(n: int) -> str:
    """"
    Meow n times
    
    :param n: Number of times to meow
    :type n: int 
    :raise TypeError: if n is not an int
    :return: A string of n meows, one per line
    :rtype: str
    """ # Added a docstring
    return "meow\n" * n

number: int = int(input("Number: "))
meows: str = meow(number)
#Brings an error whereby print(meows) prints None as the return value of meows()
#is none. mypy cat.py helps catch this error if the default return value is set to none 
print(meows, end ="")