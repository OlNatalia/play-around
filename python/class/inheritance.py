# inheritance

# general (generalisation)
# define parent class which contains all functionality that all child classes gonna inherit
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I'm {self.name} and I'm {self.age} years old.")

    def speak(self):
        print("general")  


# specific
# child classes have specific methods for own class

class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age) # call explicitly parent
        self.color = color

    def speak(self):
        print("Meow")        

    def show(self):
        print(f"I'm {self.name} and I'm {self.age} years old and I'm {self.color}.")


class Dog(Pet):
    def speak(self):
        print("Bark")   


class Fish(Pet):
    pass


# instances
p = Pet("Tim", 5)
p.show()

c = Cat("Lis", 3, "brown")
c.show()
c.speak()

d = Dog("Tom", 8)
d.show()

f = Fish("Buble", 2)
f.speak()  


# another example could be managers and employees classes that inherit from generic class Person
