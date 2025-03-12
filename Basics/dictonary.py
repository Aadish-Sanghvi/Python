# unlike sets, dictonaries are ordered 

info = {'name':'Karan', 'age':19, 'eligible':True}
print(info) 
print(info.keys())
print(info.values())
# print(info['name2']) #Error!
print(info.get('name2'))

# keys are used to access values, not vice versa.
for key in info.keys():
    print(f"The value corrosponding to the key {key} is {info[key]}")

for key, value in info.items():
    print(f"The value corresponding to the key {key} is {value}")

print("\n-------------------------DICTONARY METHODS--------------------------------")
ep1 = {122: 45, 123: 89, 567: 69, 670: 69}
ep2 = {222: 67, 566: 90}

ep1.update(ep2)
print(ep1)

ep1.pop(122)
print(ep1)
ep1.popitem() # removes last item form the dictonary
print(ep1)

ep1.clear()
print(ep1)
empt = {}
print(empt)

del ep2[222]
print(ep2)
del ep2 # delete whole dict.