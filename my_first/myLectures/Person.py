#Animal
class Person:

  def __init__(self, name, age):
    self.name = name
    self.age = age

#makeSound
  def greets(self):
    print("Hello my name is " + self.name)

#eat( food)
  def walk(self):
    print(self.name + " is walking")




p1 = Person("Souvik", 14)
p1.greets()
p1.walk()

p2 = Person("Biddu",14)
p2.greets()
p2.walk()
