import multiprocessing
import time

# Function 1: A simple task to simulate work
def task1():
    print("Code-Build started")
    time.sleep(2)  # Simulate a delay
    print("Code-Build completed")

# Function 2: Another task to simulate work
def task2():
    print("Code-Testing started")
    time.sleep(3)  # Simulate a delay
    print("Code-Testing completed")

# Function 3: Another task to simulate work
def task3():
    print("Code-Deployment started")
    time.sleep(1)  # Simulate a delay
    print("Code-Deployment completed")

# Main function to run the tasks in parallel
def main():
    # Create processes for each task
    process1 = multiprocessing.Process(target=task1)
    process2 = multiprocessing.Process(target=task2)
    process3 = multiprocessing.Process(target=task3)

    # Start the processes
    process1.start()
    process2.start()
    process3.start()

    # Wait for all processes to finish
    process1.join()
    process2.join()
    process3.join()

    print("All tasks completed.")

if __name__ == "__main__":
    main()
