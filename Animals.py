class Animal:
    def __init__(self,name,species,age):
        self.name = name 
        self.species = species
        self.age = age

    def get_info(self):
        return f"Name:{self.name}\nSpecies:{self.species}\nAge:{self.age}"
    
    
animal1 = Animal("Simba","Lion",20) 
animal2 = Animal("Dumbo","Elephant",22)
animal3 = Animal("Musa","Giraffe",17)


print(f"{animal1.get_info()}")
print(f"{animal2.get_info()}")
print(f"{animal3.get_info()}")
#("OR")
print(f"{animal1.get_info()}\n{animal2.get_info()}\n{animal3.get_info()}")