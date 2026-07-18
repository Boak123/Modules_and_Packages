import sys

if len(sys.argv) > 2:
    sys.exit("Too many arguments provided. Please provide only your name. ")
elif len(sys.argv) < 2:
    sys.exit("Too few arguments provided. Please provide your name as an argument.")
else:
    name = sys.argv[1]
    print(f"Welcome, {name}! Let's get started.")