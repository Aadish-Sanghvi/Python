import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)

hour = int(time.strftime('%H'))

if(hour >= 6 and hour < 12):
    print("Good Morning, sir")
elif(hour >= 12 and hour < 18):
    print("Good Afternoon, sir")
else:
    print("Good Evening, sir")