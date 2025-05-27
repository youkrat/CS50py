def hello():
    print("Hello", end="", sep="")

name = input("What's your name? ",).strip().title()
first, second, surname = name.split()
hello()
print(f" {first}")
print(f"Is your full name, {first} {second} {surname}?")