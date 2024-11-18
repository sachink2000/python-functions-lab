def hello():
    print("Hello, World!")

def goodbye():
    print("Goodbye, World!")

def main():
    choice = input("Enter 1 for Build or 2 for Deploy: ")
    
    if choice == "1":
        hello()
    elif choice == "2":
        goodbye()
    else:
        print("Invalid choice")

# Call main function
main()
