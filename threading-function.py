import threading

def function1():
    print("Code is building")

def function2():
    print("Code is deploying")

# Create threads
thread1 = threading.Thread(target=function1)
thread2 = threading.Thread(target=function2)

# Start threads
thread1.start()
thread2.start()

# Wait for threads to finish
thread1.join()
thread2.join()
