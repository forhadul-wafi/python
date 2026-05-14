menu = ("Tea", "Coffee", "Juice")

print("Menu:")

for i, item in enumerate(menu):
    print(i+1, item)

choice = int(input("Choose item number: "))

print("You selected:", menu[choice-1])