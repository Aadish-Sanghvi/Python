# immutable we can't change the elements of tuple
tup = (1,3,5,"green", True)
print(type(tup), tup)
print(len(tup)) 
print(tup[0])
print(tup[1])
print(tup[2])
print(tup[3])
print(tup[4])
print(tup[-2]) # 5-2 = 3 == green
if 3 in tup:
    print("Yes")
tup2 = tup[1:3]
print(tup2)


# How to change tuple indirectly 
temp = list(tup)
temp.append("India")
temp.pop(3)
temp[2] = "Pakistan"
tup = tuple(temp)
print(tup)


tuple1 = (1,2,3,4,5,3,5,1,2,1)
# res = tuple1.count(1)
# res = len(tuple1)
res = tuple1.index(1, 5, 8) # occurance of 1 from 5 to 8 indices
print(res)