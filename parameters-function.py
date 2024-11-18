def greet():
    print("Hello!")

def farewell():
    print("Goodbye!")

def call_function(func):
    func()

# Pass greet and farewell as arguments
call_function(greet)
call_function(farewell)
