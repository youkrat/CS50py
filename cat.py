def main():
    meow(1)

#Define meow
def meow(n):
    n=int(input("How many meows? "))
    while True:
        if n>0:
            break
        
    for _ in range(n):
        print("Meow")

main()