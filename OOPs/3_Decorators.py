# modify the behavior of functions and methods.
def greet(fx):
    def wrapper(*args, **kwargs): # To take the arguments from function 
        print("Good Morning!")
        fx(*args, **kwargs)
        print("Thanks...")
    return wrapper

@greet
def hello():
    print("Hello World!")

def namaste():
    print("Namaste World!")

def add(a,b):
    print(f"The sum is = {a+b}")

hello()
greet(namaste)()
greet(add)(1,2)