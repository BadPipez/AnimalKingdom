##The point of this application is to simulate nature and how animals interact with each other.
# There will be evolutionary changes that will occur over time, and the user will be able to observe these changes.
import random

print("Welcome to the Animal kingdom!")

#Here I'm creating a general class for all animals, which will hold common methods and attributes, regardless of whether the animal is 
#a predator or prey.

Animals = []
Predators = []
Herbivores = []
Grid = []


def grid(Size):
    print("grid started")
    if not Grid:
        match Size:
            case 1: ##This section creates the grid and only occurs once - at the beginning of the program
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
    Display = []    ##This section is what is called whenever the user wants to display the grid.
    count = 0               
    for i in Grid:
        occupant = i.occupant_check()  
        if occupant is not None and count!= 10:
            Display.append(f"|{occupant}| ")

            count+=1
        elif count == 10 and occupant is not None:
            Display.append(f"\n |{occupant}|" )
            count = 1
        elif count == 10 and occupant is None:
            Display.append("\n|    |")

        elif count != 10 and occupant is None:
            Display.append("|    |")
    print(Display)

        
        




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
    Answer = input("Would you like to add predators or herbivores to the simulation?")
    if Answer == "predator":
        print("Adding 5 predators to random locations.")
        match Size:
                    case 1:
                        for i in range(5):  ##The absolute peak is 100 for any stat
                            RandomX = random.randint(1,10)
                            RandomY = random.randint(1,10)
                            Grass = next(i for i in Grid if i.return_coords == RandomX and RandomY ),
                            Grass = cell("Grass", RandomX, RandomY)
                            Species = random.choice(['lion'], ['Wolf'], ['Crocodile'])
                            if Species == 'lion':
                                speed = random.randint(50,70)
                                strength = random.randint(75,100)
                                endurance = random.randint(30,60)
                                age = random.randint(1,14)
                            elif Species == 'wolf':
                                speed = random.randint(40,60)
                                strength = random.randint(20,35)
                                endurance = random.randint(20,40)
                                age = random.randint(1,13)
                            elif Species == 'crocodile':
                                speed = random.randint(45,70)
                                strength = random.randint(70,90)
                                endurance = random.randint(20,60)
                                age = random.randint(1,70)
                            x = random.randint(1,10)
                            y = random.randint(1,10)
                            Animal1 = Predator(Hunger=2,
                                               strength = strength,
                                               weapon1 = "fangs",
                                               weapon2 = "teeth",
                                               endurance = endurance,
                                               name = "Mark",
                                               species = Species,
                                               age = age,
                                               Status = "Healthy",
                                               LifeSpan= 18,
                                               speed=speed,
                                               x = x,
                                               y = y
                                               )
                            Animals.append[Animal1]
                    case 2:
                        for i in range(10):  ##The absolute peak is 100 for any stat
                            Species = random.choice(['lion'], ['Wolf'], ['Crocodile'])
                            if Species == 'lion':
                                speed = random.randint(50,70)
                                strength = random.randint(75,100)
                                endurance = random.randint(30,60)
                                age = random.randint(1,14)
                            elif Species == 'wolf':
                                speed = random.randint(40,60)
                                strength = random.randint(20,35)
                                endurance = random.randint(20,40)
                                age = random.randint(1,13)
                            elif Species == 'crocodile':
                                speed = random.randint(45,70)
                                strength = random.randint(70,90)
                                endurance = random.randint(20,60)
                                age = random.randint(1,70)
                            x = random.randint(1,25)
                            y = random.randint(1,25)
                            Animal1 = Predator(Hunger=2,
                                               strength = strength,
                                               weapon1 = "fangs",
                                               weapon2 = "teeth",
                                               endurance = endurance,
                                               name = "Mark",
                                               species = Species,
                                               age = age,
                                               Status = "Healthy",
                                               LifeSpan= 18,
                                               speed=speed,
                                               x = x,
                                               y = y
                                               )
                            Animals.append[Animal1]
                    case 3:
                        for i in range(25):  ##The absolute peak is 100 for any stat
                            Species = random.choice(['lion'], ['Wolf'], ['Crocodile'])
                            if Species == 'lion':
                                speed = random.randint(50,70)
                                strength = random.randint(75,100)
                                endurance = random.randint(30,60)
                                age = random.randint(1,14)
                            elif Species == 'wolf':
                                speed = random.randint(40,60)
                                strength = random.randint(20,35)
                                endurance = random.randint(20,40)
                                age = random.randint(1,13)
                            elif Species == 'crocodile':
                                speed = random.randint(45,70)
                                strength = random.randint(70,90)
                                endurance = random.randint(20,60)
                                age = random.randint(1,70)
                            x = random.randint(1,50)
                            y = random.randint(1,50)
                            Animal1 = Predator(Hunger=2,
                                               strength = strength,
                                               weapon1 = "fangs",
                                               weapon2 = "teeth",
                                               endurance = endurance,
                                               name = "Mark",
                                               species = Species,
                                               age = age,
                                               Status = "Healthy",
                                               LifeSpan= 18,
                                               speed=speed,
                                               x = x,
                                               y = y
                                               )
                            Animals.append[Animal1]
    else:
        print("Adding 5 herbivores")
        match Size:
            case 1:
                for i in range(5):  ##The absolute peak is 100 for any stat
                    RandomX = random.randint(1,10)
                    RandomY = random.randint(1,10)
                    Grass = next(i for i in Grid if i.return_coords == RandomX and RandomY ),
                    Grass = cell("Grass", RandomX, RandomY)
                    Species = random.choice(['Deer'], ['Rabbit'], ['Oxtail'])
                    if Species == 'Deer':
                        speed = random.randint(55,70)
                        strength = random.randint(15,25)
                        endurance = random.randint(30,65)
                        age = random.randint(1,14)
                    elif Species == 'Rabbit':
                        speed = random.randint(30,50)
                        strength = random.randint(1,5)
                        endurance = random.randint(10,30)
                        age = random.randint(1,13)
                    elif Species == 'Oxtail':
                        speed = random.randint(45,70)
                        strength = random.randint(70,90)
                        endurance = random.randint(20,60)
                        age = random.randint(1,70)
                    x = random.randint(1,10)
                    y = random.randint(1,10)
                    Animal1 = Predator(Hunger=2,
                                       strength = strength,
                                       weapon1 = "fangs",
                                       weapon2 = "teeth",
                                       endurance = endurance,
                                       name = "Mark",
                                       species = Species,
                                       age = age,
                                       Status = "Healthy",
                                       LifeSpan= 18,
                                       speed=speed,
                                       x = x,
                                       y = y
                                       )
                    Animals.append[Animal1]
            case 2:
                for i in range(10):  ##The absolute peak is 100 for any stat
                    Species = random.choice(['lion'], ['Wolf'], ['Crocodile'])
                    if Species == 'lion':
                        speed = random.randint(50,70)
                        strength = random.randint(75,100)
                        endurance = random.randint(30,60)
                        age = random.randint(1,14)
                    elif Species == 'wolf':
                        speed = random.randint(40,60)
                        strength = random.randint(20,35)
                        endurance = random.randint(20,40)
                        age = random.randint(1,13)
                    elif Species == 'crocodile':
                        speed = random.randint(45,70)
                        strength = random.randint(70,90)
                        endurance = random.randint(20,60)
                        age = random.randint(1,70)
                    x = random.randint(1,25)
                    y = random.randint(1,25)
                    Animal1 = Predator(Hunger=2,
                                       strength = strength,
                                       weapon1 = "fangs",
                                       weapon2 = "teeth",
                                       endurance = endurance,
                                       name = "Mark",
                                       species = Species,
                                       age = age,
                                       Status = "Healthy",
                                       LifeSpan= 18,
                                       speed=speed,
                                       x = x,
                                       y = y
                                       )
                    Animals.append[Animal1]
            case 3:
                for i in range(25):  ##The absolute peak is 100 for any stat
                    Species = random.choice(['lion'], ['Wolf'], ['Crocodile'])
                    if Species == 'lion':
                        speed = random.randint(50,70)
                        strength = random.randint(75,100)
                        endurance = random.randint(30,60)
                        age = random.randint(1,14)
                    elif Species == 'wolf':
                        speed = random.randint(40,60)
                        strength = random.randint(20,35)
                        endurance = random.randint(20,40)
                        age = random.randint(1,13)
                    elif Species == 'crocodile':
                        speed = random.randint(45,70)
                        strength = random.randint(70,90)
                        endurance = random.randint(20,60)
                        age = random.randint(1,70)
                    x = random.randint(1,50)
                    y = random.randint(1,50)
                    Animal1 = Predator(Hunger=2,
                                       strength = strength,
                                       weapon1 = "fangs",
                                       weapon2 = "teeth",
                                       endurance = endurance,
                                       name = "Mark",
                                       species = Species,
                                       age = age,
                                       Status = "Healthy",
                                       LifeSpan= 18,
                                       speed=speed,
                                       x = x,
                                       y = y
                                       )
                    Animals.append[Animal1]
def Skip(Size): 
    Flag = False
    while Flag == False:
        Choice = int(input("Choose an option to simulate:\n1. Skip a month\n2. Skip a year\n3. Skip a decade"))
        if Choice in [1, 2, 3]:
            Flag = True
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

    match Size:
        case 1:
            for i in Animals:
                x = random.randint(1,10)
                y = random.randint(1,10)
                i.change_coords(x,y)
                Species = i.get_species()
                SameAnimals =  (i for i in Animals if i.get_coords == x and y )
                for i in SameAnimals:
                    if i.get_species() == "herbivore" and "
                for i in
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
    def __init__(self,name, species, age,status, LifeSpan, speed, x, y):
        self.name = name
        self.species = species
        self.age = age
        self.status = status
        self.LifeSpan = LifeSpan
        self.speed = speed
        self.x = x
        self.y = y

    def get_coords(self):
        return self.x and self.y

    def Change_coords(self, x, y):
        self.x = x and self.y = y

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

    def get_species(self):
        return self.species

class Predator(Animal):
    def __init__(self, Hunger, strength, weapon1, weapon2, endurance,name, species, age,status, LifeSpan, speed, x, y):
        super().__init__(name, species, age,status, LifeSpan, speed, x, y) ##Here weapon 1 and 2 refer to fangs and claws
        self.hunger = Hunger
        self.strength = strength
        self.weapon1 = weapon1
        self.weapon2 = weapon2
        self.endurance = endurance

    def increase_strength(self):
        try:
            if self.strength != 0:
                strength+= 1

        except ValueError:
            print("Try again")
            


class herbivore(Animal):
    def __init__(self, camouflage, name, species, age,status, LifeSpan, speed, x, y):
        super().__init__(name, species, age,status, LifeSpan, speed, x, y)
        self.camouflage = camouflage

class Lion(Predator):
    def __init__(self, Hunger, strength, weapon1, weapon2, endurance, pride_size):
        super().__init__(Hunger, strength, weapon1, weapon2, endurance)
        self.pride_size = pride_size


    def Intimidate(self):
        print("The lion roars loudly to intimidate its prey.")


class Deer(herbivore):
    def __init__(self, camouflage, herd_size,name, species, age,status, LifeSpan, speed, x, y):
        super().__init__(camouflage, name, species, age,status, LifeSpan, speed, x, y)
        self.herd_size = herd_size

    def headlights(self):
        print("The deer awkwardly freezes in place")

class Wolf(Predator):
    def __init__(self, Hunger, strength, weapon1, weapon2, endurance, name, species, age, status, LifeSpan, speed, x, y, PackSize):
        super().__init__(Hunger, strength, weapon1, weapon2, endurance, name, species, age, status, LifeSpan, speed, x, y)
        self.PackSize = PackSize

    def Gather_hunt(self):
        return self.x and self.y

class Crocodile(Predator):
    def __init__(self, Hunger, strength, weapon1, weapon2, endurance, name, species, age, status, LifeSpan, speed, x, y,):
        super().__init__(Hunger, strength, weapon1, weapon2, endurance, name, species, age, status, LifeSpan, speed, x, y)

    def submerge(self):
        self.status = "submerged"

class Oxtail(Herbivores):
    def __init__(self, name, species, age,status, LifeSpan, speed, x, y):
        super().__init__(name, species, age,status, LifeSpan, speed, x, y)

class Rabbit(Herbivores):
    def __init__(self, name, species, age,status, LifeSpan, speed, x, y):
        super().__init__(name, species, age,status, LifeSpan, speed, x, y)


class cell:
    def __init__(self, occupant, x, y):
        self.occupant = occupant
        self.x = x
        self.y = y

    def occupant_check(self):
        for i in Animals:
            if self.x and self.y == i.get_coords:
                self.occupant = i.get_species
        return self.occupant

    def return_coords(self):
        return self.x and self.y
    





main()