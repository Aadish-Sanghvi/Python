class Employee:

  def __init__(self, name):
    self.name = name

  # The len method is used to get the length of an object.
  def __len__(self):
    i = 0
    for c in self.name:
      i = i + 1
    return i

  # The str and repr methods are both used to convert an object to a string representation.
  def __str__(self):
    return f"The name of the employee is {self.name} str"
  def __repr__(self):
    return f"Employee('{self.name}') repr"

  # It allows you to create objects that behave like functions.
  def __call__(self):
    print("Hey I am good")

e = Employee("Harry")
print(str(e))
print(repr(e))
e() # Call method 

# print(e.name)
# print(len(e))