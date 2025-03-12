# The yield statement returns a value from the generator and suspends the execution of
#  the function until the next value is requested.

def my_generator():
    for i in range(5):
      # Complex computations
      yield i

gen = my_generator()
print(next(gen))
print(next(gen))
print(next(gen))

gen2 = my_generator()
for i in gen2:
    print(i)