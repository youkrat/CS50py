#Added a wizard superclass with the Student and Professor subclass
class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name
    
    @classmethod
    def get(cls):
        name = input("Name: ")
        return cls(name)
    
    def __str__(self):
        return f"{self.name}"

class Student(Wizard):
    def __init__(self, name, house):
        #calls self.name from superclass wizard
        super().__init__(name)
        self.house =  house
        
        
    def __str__(self):
        return f"{self.name} from {self.house}"

    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)
    
class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject    
    
    @classmethod
    def get(cls):
        name = input("Name: ")
        subject = input("Subject: ")
        return cls(name, subject) 
    
    def __str__(self):
        return f"Prof.{self.name} teaching {self.subject}"
     

def main():
    function = int(input("Whose info?\n"
        "1 = Wizard\n"
        "2 = Student\n"
        "3 = Professor\n"))
    if function == 1:
        wizard = Wizard.get()
        print(wizard)
    elif function == 2:
        student = Student.get()
        if student.name == "Padma":
            student.house = "Ravenclaw"
        print(student)
    
    else:
        professor = Professor.get()
        print(professor)
        
        
if __name__ =="__main__":
    main()