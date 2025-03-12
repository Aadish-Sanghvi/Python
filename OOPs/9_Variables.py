# Instance Variables: They are defined inside the init method and are usually used to store information
# that is specific to each instance of the class. Here raise_amount and name are Instance var.

# Class Variables: They are defined outside of any method and are usually used to store information
# that is common to all instances of the class. Here companyName is Class var.

class Employee:
  companyName = "Apple"
  noOfEmployees = 0
  def __init__(self, name):
    self.name = name
    self.raise_amount = 0.02
    Employee.noOfEmployees += 1
  def showDetails(self):
    print(f"The name of the Employee is {self.name} and the raise amount in {self.noOfEmployees} sized {self.companyName} is {self.raise_amount}")

# Employee.showDetails(emp1)
emp1 = Employee("Harry")
emp1.raise_amount = 0.3
emp1.companyName = "Apple India" # here instance variable was declared hance name changed
emp1.showDetails()

emp2 = Employee("Rohan")
emp2.raise_amount = 0.2
emp2.showDetails()