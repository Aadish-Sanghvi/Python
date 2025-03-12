# class Employee:
#   company = "Apple"
#   def show(self):
#     print(f"The name is {self.name} and company is {self.company}")

#   @classmethod # It changes the property of class, helps to edit it permanentally
#   def changeCompany(cls, newCompany):
#     cls.company = newCompany

#     # If we run it without the classmethod then it will print Apple at the end as it will not change permanentally.

# e1 = Employee()
# e1.name = "Harry"
# e1.show()
# e1.changeCompany("Tesla")
# e1.show()
# print(Employee.company)





# Class Methods as Alternative Constructors is when you want to create an object from data that 
# is stored in a different format, such as a string or a dictionary.
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    @classmethod # Alternative constructors because it is taking diff. formate data and 
    def fromStr(cls, string):
        # return cls(string.split("-")[0], string.split("-")[1])
        name, salary = string.split("-")
        return cls(name, int(salary))

e1 = Employee("ram", 12000)
print(e1.name)
print(e1.salary)

string2 = "jay-10000"
e2 = Employee(string2.split("-")[0], string2.split("-")[1])
print(e2.name)
print(e2.salary)

string3 = "vijay-50000"
e3 = Employee.fromStr(string3)
print(e3.name, e3.salary)