class Hat:        
    def __init__(self, name):
        self.name = name
        
    def sort(self, name):
        print(name,"is in", "some house")
        
    def __getitem__ (self, index):
        return self.name[index]
        

#Instantiate(create) an object of class Hat   
hat = Hat(["Harry", "Hermione", "Ron"])

for student in hat[:3]:
    hat.sort(student)