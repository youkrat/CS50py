#Creates a class named Student
class Student:
    #Added instance variables (attributes) to the object student
    def __init__(self, name, house):
        self.name = name
        self.house =  house
        
        
    def __str__(self):
        return f"{self.name} from {self.house}"

    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)
     

def main():
    student = Student.get()
    if student.name == "Padma":
        student.house = "Ravenclaw"
    print(student)
    
if __name__ =="__main__":
    main()