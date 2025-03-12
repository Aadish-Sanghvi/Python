# f = open('myfile.txt', 'r')
# i = 0
# while True:
#   i = i + 1
#   line = f.readline()
#   if not line:
#     break
#   m1 = int(line.split(",")[0])
#   m2 = int(line.split(",")[1])
#   m3 = int(line.split(",")[2])
#   print(f"Marks of student {i} in Maths is: {m1}")
#   print(f"Marks of student {i} in English is: {m2}")
#   print(f"Marks of student {i} in SST is: {m3}")

#   print(line)



f = open('myfile2.txt', 'w')
lines = ['line1\n', 'line2\n', 'line3\n']
f.write("hello world!\n")
f.writelines(lines)   
f.truncate(15) #it will write only starting 15 bytes
f.close()



# f = open('myfile3.txt', 'r')
# # move to 5th byte in file 
# f.seek(10)
# # read next 5 bytes
# data = f.read(5)
# print(data) 
# # returns the current position within the file, in bytes
# current_position = f.tell()
# print(current_position)