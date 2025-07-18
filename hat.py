import random

class Hat: 
    #Created the class variable houses(Shared/ common in all objects)   
    houses = ["Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"]
    
    @classmethod     
    def sort(cls, name):
        print(name,"is in", random.choice(cls.houses))
        
        

#No need to instantiate the object
Hat.sort("Harry")