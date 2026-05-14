while True:
    print("--------------------------------")
    print("Chose Any option from below: ")
    print("1. Add Two Numbers: ")
    print("2. Subtract Two Numbers: ")
    print("3. Multiply Two Numbers: ")
    print("4. Divide Two Numbers: ")
    print("5. Exit The program ")

    choice = input("Enter your choice : ")
    if choice == "5":
        print("Successfully Exit!!")
        break
    if choice in ["1", "2", "3", "4"]:
        number1 = input("Enter Number One : ")
        number2 = input("Enter Number Two : ")

        if number1.isdigit() and number2.isdigit():
            num1 = int(number1)
            num2 = int(number2)

            if choice == "1":
                print(f"Sum of {num1} and {num2} is : {num1+num2} ")
            elif choice == "2":
                print(f"Sub of {num1} and {num2} is : {num1-num2}")
            elif choice == "3":
                print(f"Mult of {num1} and {num2} is : {num1*num2}")
            elif choice == "4":
                if num2 != 0:
                    print(f"Div of {num1} and {num2} is : {num1/num2}")
                else:
                    print("Cannot divide by 0")
        else:
            print("Invalid Input!")
    else:
        print("Invalid Choice")
