# Strings are immutable

name = "Harry"
apple = '''He said, 
Hi Harry
hey I am good
"I want to eat an apple'''
 
print("Hello, " + name)
# print(apple) 
print(name[0])
print(name[4])
# print(name[5]) # Throws an error
# for all in name:
#     print(all)

fruit = "Mango"
mangoLen = len(fruit)
print(mangoLen)
# print(fruit[0:4]) # including 0 but not 4
# print(fruit[1:4]) # including 1 but not 4
# print(fruit[:5])
# print(fruit[0:-3])
# print(fruit[:len(fruit)-3])
print(fruit[-3:-1])



print("\n")
print("----------------------------------- String Methods ---------------------------------")
a = "!!!Harry!! !!!!!!!!! Harry"
print(len(a))
print(a)
print(a.swapcase())
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.replace("Harry", "John"))
print(a.split(" "))
blogHeading = "introduction tO jS"
print(blogHeading.capitalize())

str1 = "Welcome to the Console!!!"
print(len(str1))
print(len(str1.center(50)))
print(a.count("Harry"))

str1 = "Welcome to the Console !!!"
print(str1.endswith("!!!"))
str1 = "Welcome to the Console !!!"
print(str1.endswith("to", 4, 10))
str1 = "Python is a Interpreted Language" 
print(str1.startswith("Python"))

str1 = "He's name is Dan. He is an honest man."
print(str1.find("issss")) # not found then -1 
print(str1.index("is"))

str1 = "WelcomeToTheConsole"
print("alpha numeric capital and small letters and numbers? ", str1.isalnum()) 
str1 = "Welcome00"
print("only alphabets? ", str1.isalpha()) 

str1 = "hello world"
print("Is in lower characters? ", str1.islower())

str1 = "We wish you a Merry Christmas\n"
print(str1.isprintable())
str1 = "         "       #using Spacebar
print("only contains white spaces? ", str1.isspace())

str1 = "World Health Organization" 
print(str1.istitle())
str2 = "To kill a Mocking bird"
print(str2.istitle())
str1 = "His name is Dan. Dan is an honest man."
print(str1.title())