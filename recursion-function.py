def countdown(n):
    if n <= 0:
        print("Done!")
    else:
        print(n)
        countdown(n-1)

# Start countdown
countdown(9)
