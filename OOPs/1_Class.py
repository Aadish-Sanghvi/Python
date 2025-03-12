class Person:
  name = "Harry"
  occupation = "Software Developer"
  networth = 10
  # When we are defining the method in a class then it's mandatory to give self argument
  def info(self):
    print(f"{self.name} is a {self.occupation}")


a = Person()
b = Person()
c = Person()

a.name = "Aadish"
a.occupation = "Accountant"

b.name = "Deshna"
b.occupation = "HR"

# print(a.name, a.occupation)
# during function calling it's not required to give self argument
a.info()
b.info()
c.info()