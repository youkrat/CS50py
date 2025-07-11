#Creates a class named Student
class Student:
    #Added instance variables (attributes) to the object student
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing name")
        self.name = name
        self.house =  house
        
        
    def __str__(self):
        return f"{self.name} from {self.house}"
    
    #Getter, and accompanying assignment syntax
    @property
    def house(self):
        return self._house
    
    #Setter and accompanying assignment syntax
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Slytherin", "Ravenclaw", "Hufflepuff"]:
            raise ValueError("Invalid house")
        self._house = house

def get_student():
    name = input("Name: ")
    house = input("House: ")
    #Constructor call(Constructs a student object from the student class
    #Equally achievable by student = student(name, house) return student
    return Student(name, house)
     

def main():
    student = get_student()
    if student.name == "Padma":
        student.house = "Ravenclaw"
    print(student)
    
if __name__ =="__main__":
    main()