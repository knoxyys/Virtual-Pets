import random

class Pet():
    def __init__(self, pet_name):
        self.name = pet_name
        self.age = 0
        self.hunger = 5
        self.boredom = 3
        self.sleepiness = 3
        self.dead = False
    
    def feed(self):
        self.hunger -= 3
        if self.hunger < 0:
            self.hunger = 0
        print(f"{self.name} has been fed. Hunger level: {self.hunger}")
    
    def play(self):
        self.boredom -= 3
        if self.boredom < 0:
            self.boredom = 0
        print(f"{self.name} has played. Boredom level: {self.boredom}")
    
    def sleep(self):
        self.sleepiness -= 5
        if self.sleepiness < 0:
            self.sleepiness = 0
        print(f"{self.name} has slept. Sleepiness level: {self.sleepiness}")
    
    def wait(self):
        self.age += 1
        self.hunger += 1
        self.boredom += 1
        self.sleepiness += 1
        print(f"{self.name} has waited. Age: {self.age}, Hunger: {self.hunger}, Boredom: {self.boredom}, Sleepiness: {self.sleepiness}")

    def check_death(self):
        if (self.boredom >= 10 or self.sleepiness >= 10 or self.hunger >= 10) and (self.age >= random.randint(15, 20)):
            self.dead = True
            print(f"{self.name} has died.")
        else:
            print(f"{self.name} is alive.")

my_pet = Pet('six')

####---Task 5----####
#make it so that the feed, sleep, play and wait will check if the pet
#is dead before you upadate those properties.

#Go to page 9 of the tutorial to learn how to make the mainline (https://classroom.google.com/w/NzE2NTQ0NzA2MTYx/t/all)