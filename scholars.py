def get_student():
    student = {}
    student["name"] = input("Name: ")
    student["house"] = input("House: ")
    return student

def main():
    student = get_student()
    print(f"{student["name"]} from {student["house"]}")

if __name__ =="__main__":
    main()