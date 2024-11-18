def multiply(a, b):
    return a * b

def add(a, b):
    return a + b

# Chain function calls using return values
result = add(multiply(2, 5), multiply(5, 5))
print(f"Result: {result}")
