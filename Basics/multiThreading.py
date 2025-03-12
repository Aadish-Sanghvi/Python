import threading
import time

def print_numbers(name):
    for i in range(5):
        print(f"{name}:{i} ")
        time.sleep(1)
        
print("Normal code")
print_numbers("Thread1")
print_numbers("Thread2")

# Create threads
thread1 = threading.Thread(target=print_numbers, args=("Thread1",))
thread2 = threading.Thread(target=print_numbers, args=("Thread2",))

# Start threads
thread1.start()
thread2.start()

# Wait for threads to complete before proceeding.
thread1.join()
thread2.join()

print("Both threads have finished execution.")
