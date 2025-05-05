import random

class Pet():
    def __init__(self, pet_name):
        self.name = pet_name
        self.age = 0
        self.hunger = 5
        self.boredom = 3
        self.sleepiness = 3
        self.dead = False
    
    def __str__(self):
        return f"Pet Name: {self.name}, Age: {self.age}, Hunger: {self.hunger}, Boredom: {self.boredom}, Sleepiness: {self.sleepiness}, Dead: {self.dead}"
    
    def feed(self):
        if self.dead:
            print(f"{self.name} is dead and cannot be fed.")
            return
        self.hunger -= 3
        if self.hunger < 0:
            self.hunger = 0
        print(f"{self.name} has been fed. Hunger level: {self.hunger}")
    
    def play(self):
        if self.dead:
            print(f"{self.name} is dead and cannot play.")
            return
        self.boredom -= 3
        if self.boredom < 0:
            self.boredom = 0
        print(f"{self.name} has played. Boredom level: {self.boredom}")
    
    def sleep(self):
        if self.dead:
            print(f"{self.name} is dead and cannot sleep.")
            return
        self.sleepiness -= 5
        if self.sleepiness < 0:
            self.sleepiness = 0
        print(f"{self.name} has slept. Sleepiness level: {self.sleepiness}")
    
    def wait(self):
        if self.dead:
            print(f"{self.name} is dead and cannot wait.")
            return
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

my_pet = Pet(input("What is your pet's name? "))
print(my_pet)

action = input("What would you like to do with your pet? ").lower()
while action != '':
    print("-----------------------------------------------------")
    print(my_pet)
    print("-----------------------------------------------------")
    action = input("What do you want to do with your pet? ")

    # go off page 9 from here (https://classroom.google.com/w/NzE2NTQ0NzA2MTYx/t/all)