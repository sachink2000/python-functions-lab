def square(x):
    return x * x

def cube(x):
    return x * x * x

# List of numbers
numbers = [1, 2, 3, 4, 5]

# Apply square and cube using map
squares = list(map(square, numbers))
cubes = list(map(cube, numbers))

print("Squares:", squares)
print("Cubes:", cubes)
