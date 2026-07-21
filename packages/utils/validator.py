def get_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            return("Error: Invalid input. Please enter a valid number.")
        else:
            break

        