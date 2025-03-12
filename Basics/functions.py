def calculateGmean(a,b):
    '''takes in 2 numbers and calculates their Gmean''' # Doc string always below the fun name and above fun def.
    mean = (a*b)/(a+b)
    print(mean)
a = 9
b = 8
calculateGmean(a,b)
print(calculateGmean.__doc__) # we can print doc string of a function

def functions(a):
    pass # Will write it later...


# def average(a, b, c=1):
#   print("The average is ", (a + b + c) / 2)
# average(4, 6)
# average(b=9)

def average(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    # print("The average is: ", sum/len(numbers))
    return sum/len(numbers)

c = average(1,2,3,4,5)
print(c)



# lambda functions -> we use it when passing function as argument
def apply(fun, value):
    return 10 + fun(value)

double = lambda x: x*2
average = lambda x,y: (x+y)/2

print(double(100))
print(average(3,5))
print(apply(double, 10)) # 10+20 = 30