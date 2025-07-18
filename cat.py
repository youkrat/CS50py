#Added a type hint to let the program know that n should be an int
#-> str hints that the return value of meow should be str
def meow(n: int) -> str:
    return "meow\n" * n

number: int = int(input("Number: "))
meows: str = meow(number)
#Brings an error whereby print(meows) prints None as the return value of meows()
#is none. mypy cat.py helps catch this error if the default return value is set to none 
print(meows, end ="")