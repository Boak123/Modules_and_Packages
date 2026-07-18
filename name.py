import sys

name = sys.argv[1]
if len(sys.argv) > 2:
    print("Too many arguments provided. Please provide only your name. ")
elif len(sys.argv) < 2:
    print("Too few arguments provided. Please provide your name as an argument.")
else:
    print(f"Welcome, {name}! Let's get started.")