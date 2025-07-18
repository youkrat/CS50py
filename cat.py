#Added a type hint to let the program know that n should be an int
#-> None hints that the return value of meow should be None 
def meow(n: int) -> None:
    for _ in range(n):
        print("Meow")

number: int = int(input("Number: "))
meows: str = meow(number)
#Brings an error whereby print(meows) prints None as the return value of meows()
#is none. mypy cat.py helps catch this error if the default return value is set to none 
print(meows)