# class Employee:
#     def __init__(self, name, id):
#         self.name = name
#         self.id = id

#     def showInfo(self):
#         print(f"The name of employee is: {self.name} and his ID is: {self.id}")

# class Child(Employee): # Now this class has all the attributes of it's parent class 
#     def showSomething(self):
#         print("This is derieved class")
    
# e1 = Employee("Hapsi", 420)
# e1.showInfo()

# e2 = Child("Aadish", 777)
# e2.showInfo()
# e2.showSomething()
# print(e2.id)




# Single Inheritance ------------------------------------------------------------
# class Animal:
#     def __init__(self, name, species):
#         self.name = name
#         self.species = species

#     def make_sound(self):
#         print("Sound made by Animal.")

# class Dog(Animal):
#     def __init__(self, name, breed):
#         Animal.__init__(self, name, species = "Dog")
#         self.breed = breed

#     def make_sound(self):
#         print("Bark!")

# class Cat(Animal):
#     def __init__(self, name, breed):
#         Animal.__init__(self, name, species = "Cat")
#         self.breed = breed
    
#     def make_sound(self):
#         print("Mewww!")
    
#     def dance(self):
#         print("cat dancing")
        
# d = Dog("dog", "pug")
# d.make_sound()

# a = Animal("cat", "german")
# a.make_sound()

# c = Cat("cat", "afgaani")
# c.make_sound()
# c.dance()




# Multiple Inheritance ------------------------------------------------------------
# class Employee:
#     def __init__(self, name):
#         self.name = name
#     def show(self):
#         print(f"The name is {self.name}")
    
# class Dancer:
#     def __init__(self, dance):
#         self.dance = dance
#     def show(self):
#         print(f"The dance is {self.dance}")

# class DancerEmployee(Dancer, Employee): # The function of class which is inherited first will be called.
#     def __init__(self, dance, name):
#         self.dance = dance
#         self.name = name

# o = DancerEmployee("Break Dance", "Aadish")
# print(o.name)
# print(o.dance)
# o.show()




# Multilevel Inheritance ------------------------------------------------------------
# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def move(self):
#         print(f"{self.name} moves")

# class Mammal(Animal):
#     def __init__(self, name, has_fur):
#         super().__init__(name)
#         self.has_fur = has_fur

#     def feed_milk(self):
#         print(f"{self.name} feeds milk")

# class Dog(Mammal):
#     def __init__(self, name, has_fur, breed):
#         super().__init__(name, has_fur)
#         self.breed = breed

#     def bark(self):
#         print(f"{self.name} barks")

# # Create an instance of Dog
# dog = Dog("Buddy", True, "Golden Retriever")

# # Call methods from all levels of the inheritance chain
# dog.move()       # Inherited from Animal
# dog.feed_milk()  # Inherited from Mammal
# dog.bark()       # Defined in Dog

# print(f"Name: {dog.name}, Has Fur: {dog.has_fur}, Breed: {dog.breed}")




# Hybrid Inheritance ------------------------------------------------------------
# class Vehicle:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

#     def start(self):
#         print(f"{self.brand} {self.model} is starting.")

# class Car(Vehicle):
#     def __init__(self, brand, model, seats):
#         super().__init__(brand, model)
#         self.seats = seats

#     def drive(self):
#         print(f"{self.brand} {self.model} is {self.seats} seater")

# class Truck(Vehicle):
#     def __init__(self, brand, model, cargo_capacity):
#         super().__init__(brand, model)
#         self.cargo_capacity = cargo_capacity

#     def haul(self):
#         print(f"{self.brand} {self.model} with cargo capacity of {self.cargo_capacity} tons is hauling.")

# class Hybrid(Car, Truck):
#     def __init__(self, brand, model, seats, cargo_capacity, fuel_efficiency):
#         Vehicle.__init__(self, brand, model)
#         self.seats = seats
#         self.cargo_capacity = cargo_capacity
#         self.fuel_efficiency = fuel_efficiency

#     def display(self):
#         print(f"{self.brand} {self.model} with {self.seats} seats and {self.cargo_capacity} tons cargo capacity has fuel efficiency of {self.fuel_efficiency} km/l.")

# # Create an instance of Hybrid
# hybrid_vehicle = Hybrid("Toyota", "Prius", 4, 1.5, 22.0)

# # Call methods from all levels of the inheritance chain
# hybrid_vehicle.start()       # Inherited from Vehicle
# hybrid_vehicle.drive()       # Inherited from Car
# hybrid_vehicle.haul()        # Inherited from Truck
# hybrid_vehicle.display()     # Defined in Hybrid




# Hierarchical Inheritance ------------------------------------------------------------
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

class Cow(Animal):
    def speak(self):
        return f"{self.name} says Moo!"

# Creating instances of the child classes
dog = Dog("Buddy")
cat = Cat("Whiskers")
cow = Cow("Bessie")

# Calling the speak method for each instance
print(dog.speak())
print(cat.speak())
print(cow.speak())