#Creates a class named Student
class Student:
    #Added instance variables to the object student
    def __init__(self,name,house):
        self.name = name
        self.house =  house


def get_student():
    name = input("Name: ")
    house = input("House: ")
    #Constructor call. Constructs a student object 
    student = Student(name,house)
    return student

def main():
    student = get_student()
    if student.name == "Padma":
        student.house = "Ravenclaw"
    print(f"{student.name} from {student.house}")

if __name__ =="__main__":
    main()