num1 = input("Enter number one : ")
num2 = input("Enter number two: ")
op = input("Enter any operation (+,-,/,*,%) : ")

try:
    n1 = float(num1)
    n2 = float(num2)

    if op == "+":
        print(f"Sum is : {n1+n2}")
    elif op == "-":
        print(f"Sub is : {n1-n2}")
    elif op == "/":
        if n2 == 0:
            print(f"Operation not possible")
        else:
            print(f"Div is : {n1/n2}")
    elif op == "*":
        print(f"Mult is : {n1*n2}")
    elif op == "%":
        print(f"Mod is : {n1%n2}")
    else:
        print(f"Invalid iOperator")

except:
    print(f"Wrong Input")
