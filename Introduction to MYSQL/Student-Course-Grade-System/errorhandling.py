def name_errorhandling(prompt):
    while True:
        value = input(prompt).strip() # Gets input removes spaces
        if not value: # Checks if there is input
            print("Name cannot be empty")
            continue
        if not value.isalpha():
            print("Name must have only letters.")
            continue
        return value

def int_errorhandling(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid Number")