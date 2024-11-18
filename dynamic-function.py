def build():
    print("Code is building")

def deploy():
    print("Code is deploying")

# Store functions in a list
functions = [build, deploy]

# Call each function in the list
for func in functions:
    func()
