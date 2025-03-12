# Public Members: Accessible from anywhere---------------------------------------------------
# class Parent:
#     def __init__(self, name):
#         self.name = name  # Public attribute
    
#     def show_name(self):
#         print(self.name)  # Public method

# class Child(Parent):
#     def show_parent_name(self):
#         self.show_name()  # Accessing parent's public method

# # Example usage
# parent = Parent("Parent Name")
# child = Child("Child Name")

# print(parent.name)  # Accessing public attribute
# child.show_parent_name()  # Accessing public method from parent class
# parent.show_name()

# PROTECTED accessible within the class and its subclasses -----------------------------------
# class Parent:
#     def __init__(self, name, age):
#         self._name = name  # Protected attribute
#         self._age = age

#     def _show_name(self):  # Protected method
#         print(self._name)
        
# class Child(Parent):
#     def show_parent_name(self):
#         self._show_name()  # Accessing parent's protected method

# # Example usage
# parent = Parent("Parent Name", 50)
# child = Child("Child Name", 25)

# print(parent._name)  # Technically accessible but treated as protected
# print(parent._age)
# parent._show_name()
# print(child._age)
# child.show_parent_name()  # Accessing protected method from parent class

# PRIVATE: intended to be accessed only within the class-------------------------------------
class Parent:
    def __init__(self, name, age, secret):
        self.__name = name  # Private attribute
        self.__age = age
        self.__secret = secret

    def __show_secret(self):  # Private method
        print(self.__secret)

    def get_secret(self):   # Public method
        return self.__secret

class Child(Parent):
    def reveal_secret(self):
        # self.__show_secret()  # This will raise an AttributeError
        print(self.get_secret())  # Accessing private attribute through public method

# Example usage
parent = Parent("Parent Name", 50, "Secret")
child = Child("Child Name", 25, "Child Secret")

# print(parent.__name)  # This will raise an AttributeError
child.reveal_secret()  # Accessing private attribute through inherited public method