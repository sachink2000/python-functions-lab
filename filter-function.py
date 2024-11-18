def is_even(x): 
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# Filter even numbers using filter()
even_numbers = list(filter(is_even, numbers)) 

print("Even numbers:", even_numbers)
