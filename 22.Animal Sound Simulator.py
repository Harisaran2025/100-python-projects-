#animal sound simulator
class Animal:
  def make_sound(self):
    print("Animal sound")

class Dog(Animal):
  def make_sound(self):
    print("Woof! Woof!")

class Cat(Animal):
  def make_sound(self):
    print("meow! meow!")

class Cow(Animal):
  def make_sound(self):
    print("Moo! Moo!")

class Duck(Animal):
  def make_sound(self):
    print("Quack! Quack!")

class AnimalSoundSimulator:
  def __init__(self):
    self.animals = []

  def add_animal(self,animal):
    if isinstance(animal,Animal):
      self.animals.append(animal)
      print(f"{animal.__class__.__name__} added to the simulator")
    else:
      print("Invalid animal type")

  def make_all_animals_sound(self):
    if not self.animals:
      print("No animals in the simulator")
    else:
      print("\n-----Animal Sound Simulator-----")
      for animal in self.animals:
        animal.make_sound()

simulator = AnimalSoundSimulator()

while True:
  print("\n-----Animal Sound Simulator Menu-----")
  print("1. Add Dog ")
  print("2. Add Cat")
  print("3. Add Cow")
  print("4. Add Duck")
  print("5. Make All Animals Sound")
  print("6. Exit")
  choice = int(input("Enter your choice (1/2/3/4/5/6): ").strip())
  if choice == 1:
    simulator.add_animal(Dog())
  elif choice == 2:
    simulator.add_animal(Cat())
  elif choice == 3:
    simulator.add_animal(Cow())
  elif choice == 4:
    simulator.add_animal(Duck())
  elif choice == 5:
    simulator.make_all_animals_sound()
  elif choice == 6:
    print("Exiting Animal Sound Simulator")
    break
  else:
    print("Invalid choice")
