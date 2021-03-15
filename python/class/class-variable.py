# class atributtes

class Person:
    # class atributtes
    num_of_people = 0

    def __init__(self, name):
        self.name = name
        # Person.num_of_people += 1
        Person.add_person()

    # function methods referencing the class
    @classmethod
    def number_of_people(cls):
        return cls.num_of_people

    @classmethod
    def add_person(cls):
        cls.num_of_people += 1


p1 = Person("Tim")
p2 = Person("Tom")
# print(Person.num_of_people)
print(Person.number_of_people())
