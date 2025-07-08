def get_student():
    name=input("What's your name? ")
    house=input("What's your house? ")
    #Used a tuple(data type in python) Unchangeable/Immutable
    return name,house

def main():
    name,house=get_student()
    print(f"{name} from {house}")

if __name__ =="__main__":
    main()