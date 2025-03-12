# MAP
def cube(x):
    return x*x*x

l = [0,2,4,6,8]

# newl = []
# for i in l:
#     newl.append(cube(i))

newl = list(map(cube, l))
print(newl)

# FILTER
def filter_function(a):
    return a>4
newnewl = list(filter(filter_function, l))
print(newnewl)


from functools import reduce
number = [1,2,3,4,5]
sum = reduce(lambda x,y: x+y, number)
fact = reduce(lambda x,y: x*y, number)
print("Sum is: ", sum)
print("Factorial is: ", fact)