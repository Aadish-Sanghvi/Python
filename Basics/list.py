# Mutable
marks = [3, 5, 6, "Harry", True, 6, 7 , 2, 32, 345, 23]

if 365 in marks: 
    print("Yes")
else:
    print("No")

# list comprehension
lst = [i for i in range(4)]
print(lst)

lst = [i*i for i in range(10) if i%2 == 0]
print(lst)


print("\n---------------------------- List methons ----------------------------")
l = [11, 45, 1, 2, 4, 6, 1, 1]
l.append(7)
l.sort(reverse=True) #desc
l.sort() #asc
l.reverse() #rev
print(l.index(1))
print(l.count(1))

m = l.copy()
m[0] = 0
l.insert(1, 899)
k = l + m
print(k)
m = [900, 1000, 1100]
l.extend(m)
print(l)