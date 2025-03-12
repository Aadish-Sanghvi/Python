# name = 'Aadish'
# for i in name:
#     print(i)
#     if(i == "i"):
#         print("got it!")



# colors = ["Red", "Green", "Black", "Blue"]
# for color in colors:
#     if(color != "Black"):
#         print(color)
#     if(color == "Black"):
#         for i in color:
#             print(i)




# for loop 
print("\nFor Loop")
for k in range(1,10,5): #[1,n-1, increment]
    print(k)

print("\n")
# we can use else in for loop 
for i in range(6):
  print("iteration no {} in for loop".format(i+1))
  # if(i == 4):
  #   break
else:
  print("else block in loop") # After break statement else will not run...
print ("Out of loop")


# while loop
print("\nWhile Loop")
i = 0
while(i <= 3):
    print(i)
    i = i+1
count = 5
while (count > 0):
  print(count)
  count = count - 1
else:
  print("I am inside else")


print("\ncontinue statement")
for i in range(12):
  if(i == 10):
    print("Skip the iteration")
    continue
    print("iske niche ka kuch bhi execute nhi hoga")
  print("5 X", i, "=", 5 * i)

print("\nBreak statement")
for i in range(12):
  if(i == 5):
    break
  print("5 X", i, "=", 5 * i)





# Do while loop in python
print("\nDo While loop in python")
i = 0
while True:
  print(i)
  i = i + 1
  if(i%5 == 0):
    break


# Enumerate function -> gives indices with values in secquence at same time 
print("\nEnumerate function")
marks = [11,12,13,14,15,16,17,18,19]

# index = 0
# for mark in marks:
#   print(mark)
#   if(index == 3):
#     print("Harry, awesome!")
#   index +=1

for index, marks in enumerate(marks, start = 1):
  print(index, marks)
  if(index == 3):
    print("Good Work!")
