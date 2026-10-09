##The point of this application is to simulate nature and how animals interact with each other.
# There will be evolutionary changes that will occur over time, and the user will be able to observe these changes.


print("Welcome to the Animal kingdom!")
print("How are you?")

#Here I'm creating a general class for all animals, which will hold common methods and attributes, regardless of whether the animal is 
#a predator or prey.

Animals = []
Predators = []
Herbivores = []
Grid = []

def main():
    while True:
        try:
            Size = int(input("Please enter the size of the grid: 10x10, 25x25, 100x100 "))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            
            

def Simulation():
    print("Choose an option to simulate:")
    print("1. Skip a month")
    print("2. Skip a year")
    print("3. Skip a decade")



class Animal:
    def __init__(self,name, species, age,status, LifeSpan, speed):
        self.name = name
        self.species = species
        self.age = age
        self.status = status
        self.LifeSpan = LifeSpan
        self.speed = speed

    def get_age(self):
        return self.age

    def get_status(self):
        return self.status

    def get_LifeSpan(self):
        return self.LifeSpan

    def get_speed(self):
        return self.speed

class Predator(Animal):
    def __init__(self, Hunger, strength, weapon1, weapon2, endurance): ##Here weapon 1 and 2 refer to fangs and claws
        self.hunger = Hunger
        self.strength = strength
        self.weapon1 = weapon1
        self.weapon2 = weapon2
        self.endurance = endurance

class herbivore(Animal):
    def __init__(self, camouflage):
        self.camouflage = camouflage