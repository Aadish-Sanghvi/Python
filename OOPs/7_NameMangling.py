class Parent:
    def __init__(self, name):
        self.__name = name  # Private attribute

    def __show_name(self):  # Private method
        print(self.__name)

    def get_name(self):  # Public method to access private attribute
        return self.__name

class Child(Parent):
    def reveal_name(self):
        # Trying to access the private method directly will raise an AttributeError
        # self.__show_name()  # This will raise an AttributeError
        
        # Accessing private attribute through public method
        print(self.get_name())

# Example usage
parent = Parent("Parent Name")
child = Child("Child Name")

# Direct access to the private attribute will raise an AttributeError
# print(parent.__name)  # This will raise an AttributeError

# Direct access to the private method will raise an AttributeError
# parent.__show_name()  # This will raise an AttributeError

# Accessing private attribute using name mangling
print(parent._Parent__name)  # Accessing the mangled name

# Accessing private method using name mangling
parent._Parent__show_name()  # Accessing the mangled method

# Using the public method to access the private attribute
child.reveal_name()