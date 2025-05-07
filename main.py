import random

class Pet():
    def __init__(self, pet_name):
        self.name = pet_name
        self.age = 0
        self.hunger = 5
        self.boredom = 3
        self.sleepiness = 3
        self.__dead = False
    
    def __str__(self):
        return f"Pet Name: {self.name}, Age: {self.age}, Hunger: {self.hunger}, Boredom: {self.boredom}, Sleepiness: {self.sleepiness}, Dead: {self._Pet__dead}"
    
    def feed(self):
        if self._Pet__dead:
            print(f"{self.name} is dead and cannot be fed.")
            return
        self.hunger -= 3
        if self.hunger < 0:
            self.hunger = 0
        print(f"{self.name} has been fed. Hunger level: {self.hunger}")
    
    def play(self):
        if self._Pet__dead:
            print(f"{self.name} is dead and cannot play.")
            return
        self.boredom -= 3
        if self.boredom < 0:
            self.boredom = 0
        print(f"{self.name} has played. Boredom level: {self.boredom}")
    
    def sleep(self):
        if self._Pet__dead:
            print(f"{self.name} is dead and cannot sleep.")
            return
        self.sleepiness -= 5
        if self.sleepiness < 0:
            self.sleepiness = 0
        print(f"{self.name} has slept. Sleepiness level: {self.sleepiness}")
    
    def wait(self):
        if self._Pet__dead:
            print(f"{self.name} is dead and cannot wait.")
            return
        self.age += 1
        self.hunger += 1
        self.boredom += 1
        self.sleepiness += 1
        print(f"{self.name} has waited.")

    def check_death(self):
        if (self.boredom >= 10 or self.sleepiness >= 10 or self.hunger >= 10) or (self.age >= random.randint(15, 20)):
            self._Pet__dead = True
            return True
        else:
            print(f"{self.name} is alive.")

my_pet = Pet(input("What is your pet's name? "))

action = ' '
while action != '':
    action = input("What do you want to do with your pet? ")
    if action == "kill":
        my_pet.dead = True
    if action == "feed":
        my_pet.feed()
    if action == "play":
        my_pet.play()
    if action == "sleep":
        my_pet.sleep()
    if action == "wait":
        my_pet.wait()
    else:
        print("You can only choose to feed, play, sleep or wait. ")
    if my_pet.check_death() == True:
        print(f"❗❗❗❗❗❗❗❗❗❗❗{my_pet.name} has died.❗❗❗❗❗❗❗❗❗❗❗")
        print("-----------------------------------------------------------------------------------")
        print(my_pet)
        print("-----------------------------------------------------------------------------------")
        break
    print("-----------------------------------------------------------------------------------")
    print(my_pet)
    print("-----------------------------------------------------------------------------------")


    # go off page 9 from here (https://classroom.google.com/w/NzE2NTQ0NzA2MTYx/t/all)