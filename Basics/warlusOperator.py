# walrus operator := assigns values to variables as part of a larger expression

happy = False
print(happy)
print(happy := True)


foods = list()
# Without warlus
while True:
  food = input("What food do you like?: ")
  if food == "quit":
      break
  foods.append(food)
foods = list()

# With warlus
while (food := input("What food do you like?: ")) != "quit":
    foods.append(food)