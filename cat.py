def main():
    number = get_number()
    meow(number)

#Define get_number
def get_number():
    while True:
        n=int(input("How many meows? "))
        if n>0:
            return n

#Define meow
def meow(n):
    for _ in range(n):
        print("Meow")
main()