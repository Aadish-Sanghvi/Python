from functools import lru_cache
import time

# cache memory is deleted after the program execution is done.
@lru_cache(maxsize=None)
def fx(n):
  time.sleep(3)
  return n*5
    

print(fx(20))
print("done for 20")
print(fx(2))
print("done for 2")
print(fx(6))
print("done for 6")

print(fx(20))
print("done for 20")
print(fx(2))
print("done for 2")
print(fx(6))
print("done for 6")

print(fx(61))
print("done for 61")