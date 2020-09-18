class Person:
    number_of_people = 0

    def __init__(self,name):
        self.name = name
        Person.add_people()


    @classmethod
    def People_Number(cls):
        return cls.number_of_people
    
    @classmethod
    def add_people(cls):
        cls.number_of_people += 1

p1 = Person("Tim")
p2 = Person("Jill")

print(Person.People_Number())

# Classmethod = function related to that class and that class only. Use this type when you are using values of the class, not the instance 
# (For example, using a class that retrieves the total count of instances of that Class created and stored in a class variable). 
# You don't need to create one instance to use it.