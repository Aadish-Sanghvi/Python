a = int(input("Enter any age "))
print("Your age is: ", a)

if(a >= 18):
    print("You and drive and vote")
else:
    print("You can't drive and vote")


# Elif
num = int(input("Enter the value of num: "))
if (num < 0):
  print("Number is negative.")
elif (num == 0):
  print("Number is Zero.")
elif (num == 999):
  print("Number is Special.")
else:
  print("Number is positive.")

print("I am happy now")


# NESTED IF-ELSE
num = 18
if (num < 0):
    print("Number is negative.")
elif (num > 0):
    if (num <= 10):
        print("Number is between 1-10")
    elif (num > 10 and num <= 20):
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")


# ShortHand
a = 3330
b = 350
print("A") if a > b else print("=") if a == b else print("B") 

c = 9 if a>b else 0
print(c)