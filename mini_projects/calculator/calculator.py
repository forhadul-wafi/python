# Basic arithmetic functions
def addition(a, b):
    return a + b  # returns sum of two numbers

def subtraction(a, b):
    return a - b  # returns difference

def division(a, b):
    return a / b  # returns division result

def multiplication(a, b):   
    return a * b  # returns product

def power(a,b):
    return a**b  # exponentiation (a raised to b)

def modulus(a,b):
    return a % b  # remainder after division

def floor_division(a,b):
    return a // b  # integer division (removes decimal part)

# mapping user choice to function
operations = {
    1: addition,
    2: subtraction,
    3: division,
    4: multiplication,
    5: power,
    6: modulus,
    7: floor_division
}

# stores calculation history
history = []

# infinite loop for calculator menu
while True:
    print("\nChoose one from below:")
    print("1) Addition")
    print("2) Subtraction")
    print("3) Division")
    print("4) Multiplication")
    print("5) Power")
    print("6) Modulus")
    print("7) Floor Division")
    print("8) Show history")
    print("9) Exit")

    try:
        choice = int(input("Enter your choice: "))

        # exit program
        if choice == 9:
            print("Program exit successful")
            break

        # show calculation history
        if choice == 8:
            print("\n--- Calculation History ---")
            if not history:
                print("No history yet.")
            else:
                for item in history:
                    print(item)
            continue

        # invalid menu selection
        if choice not in operations:
            print("Invalid choice")
            continue

        # input numbers
        x = float(input("Enter the first number: "))
        y = float(input("Enter the second number: "))

        # prevent division/modulo/floor division by zero
        if choice in [3, 6, 7]:
            while y == 0:
                print("Error: Second number cannot be zero for this operation.")
                y = float(input("Enter a non-zero second number: "))

        # perform operation dynamically using dictionary
        result = operations[choice](x,y)

        print(f"Your result is {result:.2f}")

        # operator symbols for history
        symbols = {
            1: "+",
            2: "-",
            3: "/",
            4: "*",
            5: "**",
            6: "%",
            7: "//"
        }

        # store formatted history entry
        history.append(f"{x} {symbols[choice]} {y} = {result:.2f}")

    except ValueError:
        # handles invalid input like strings instead of numbers
        print("Enter a valid numeric input")