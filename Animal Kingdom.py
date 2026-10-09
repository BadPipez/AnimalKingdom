##The point of this application is to simulate nature and how animals interact with each other.
# There will be evolutionary changes that will occur over time, and the user will be able to observe these changes.
import random

print("Welcome to the Animal kingdom!")
print("How are you?")

#Here I'm creating a general class for all animals, which will hold common methods and attributes, regardless of whether the animal is 
#a predator or prey.

Animals = []
Predators = []
Herbivores = []
Grid = []


def grid(Size):
    if not Grid:
        match Size:
            case 1:
                for i in range(10):
                    for j in range(10):
                        cell_instance = cell(None, i, j)
                        Grid.append(cell_instance)
            case 2:
                for i in range(25):
                    for j in range(25):
                        cell_instance = cell(None, i, j)
                        Grid.append(cell_instance)
            case 3:
                for i in range(50):
                    for j in range(50):
                        cell_instance = cell(None, i, j)
                        Grid.append(cell_instance)
    Display = ""     
    count = 0               
    for i in Grid:
        occupant = i.occupant_check  
        if occupant is not None and count!= 10:
            Display.append(f"|{occupant}| ")
        else:
            Display.append("\n|    |")
        count+=1
        if count == 10:
            Display.append( )
        




def main():
    while True:
        try:
            Size = int(input("Please enter the size of the grid: 10x10\n25x25\n50x50 "))
            break  ##Here I realized that without this break, the loop would continue forever regardless of user input, so i add a break statement 
        #to exit the loop once a valid input is received.
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    Simulation(Size)
            
            

def Simulation(Size):
    Flag = False
    while Flag == False:
        Choice = int(input("Choose an option to simulate:\n1. Skip a month\n2. Skip a year\n3. Skip a decade"))
        if Choice in [1, 2, 3]:
            Flag = True
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

    match Size:
        case 1:
            for i in range(10):
                print("|   |   |   |   |   |   |   |   |   |   |")
        case 2:
            for i in range(25):
                print("|   |   |   |   |   |   |   |   |   |   |  |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |")
        case 3:
            for i in range(50):
                print("|   |   |   |   |   |   |   |   |   |   |  |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |  |   |   |   |   |   |   |   |   |   |   |  |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |")       

##All this should be in the grid. I should have a method called grid which holds cells which are created based on the size of the grid.
## Each cell should be constructed from the cell class and then appended to the grid list. 
##Cell should display the format but also look inside to see if there is an animal, in which case it should also display the animal's species
#Only issue is idk how to do that yet. I think I need to create a method in the cell class that checks if there is an animal in the cell, and if so, it should display the animal's species.
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

    def Intimidate(self):
        print("intimidating tactic") ## I plan to use polymorphism for different intimidation tactics for different species.

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

class Lion(Predator):
    def __init__(self, Hunger, strength, weapon1, weapon2, endurance, pride_size):
        super().__init__(Hunger, strength, weapon1, weapon2, endurance)
        self.pride_size = pride_size


    def Intimidate(self):
        print("The lion roars loudly to intimidate its prey.")


class Deer(herbivore):
    def __init__(self, camouflage, herd_size):
        super().__init__(camouflage)
        self.herd_size = herd_size

    def headlights(self):
        print("The deer awkwardly freezes in place")


class cell:
    def __init__(self, occupant, x, y):
        self.occupant = occupant
        self.x = x
        self.y = y

    def occupant_check(self):
        return self.occupant




main()