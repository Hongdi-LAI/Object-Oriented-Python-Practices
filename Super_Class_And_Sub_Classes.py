class Pets:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def show(self):
        # f string allows to have variable insert
        print(f"I am {self.name} and I am {self.age} years old")

    def speak(self):
        print("I dont know how I sound like :(")

class Cat(Pets):
    def __init__(self,name,age,color):
        # referencing the upper class Pets
        super().__init__(name,age)
        self.color = color

    # although in the upper class there is a speak() as well
    # it will be overrided by this function down below in this specific class
    def speak(self):
        print("Meow")

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and I am {self.color}")

class Dog(Pets):
    def speak(self):
        print("Woof")

p = Pets("Lily",2)
p.speak()
p.show()

cat1 = Cat("Jewel",3,"balck")
# overriding the upper class show() function
cat1.show()
             
dog1 = Dog("Buggy",4)
# referencing upper class show() function
dog1.show()

