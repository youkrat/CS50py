#Creates a class named Student
class Student:
    #Added instance variables (attributes) to the object student
    def __init__(self, name, house, patronus):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        if not patronus:
            raise ValueError("Missing patronus")
        self.name = name
        self.house =  house
        self.patronus = patronus
        
        
    def __str__(self):
        return f"{self.name} from {self.house} with the {self.patronus} patronus"
    
    def charm(self):
        match self.patronus:
            case "Stag":
                return "🐎"
            case "Otter":
                return "🦦"
            case "Jack Russel Terrier":
                return "🦮"
            case _:
                return "🎆"

def get_student():
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
    #Constructor call. Constructs a student object 
    return Student(name, house, patronus)
     

def main():
    student = get_student()
    if student.name == "Padma":
        student.house = "Ravenclaw"
    print("Expecto patronum")
    print(student.charm())
    
if __name__ =="__main__":
    main()