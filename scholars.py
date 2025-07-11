#Creates a class named Student
class Student:
    #Added instance variables to the object student
    def __init__(self, name ,house):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house =  house
        
    def __str__(self):
        return f"{self.name} from {self.house}"
        

def get_student():
    name = input("Name: ")
    house = input("House: ")
    #Constructor call. Constructs a student object 
    return Student(name,house)
     

def main():
    student = get_student()
    if student.name == "Padma":
        student.house = "Ravenclaw"
    print(student)

if __name__ =="__main__":
    main()