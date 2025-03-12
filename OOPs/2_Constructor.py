class person:
    # Parameterised Constructor
    def __init__(self, n, o):
        print("Hey! i am a person")
        self.name = n
        self.occ = o

    def info(self):
        print(f"{self.name} is {self.occ}")

    # rather predefining these we should pass name and occ directly which is done by constructor.
    # name = "Aadish"
    # occ = "HR"

class person2:
    # Default Constructor
    def __init__(self):
        print("Hey! i am a default Constructor")

# during constructor call it's not required to pass self, self is automatically passed as a,b
c = person2()
a = person("Aadish", "HR")
b = person("Adiiii", "Developer")
a.info()
b.info()