actual_number = 12
guess = input("Enter your number : ");

if guess.isdigit():
  com_num = int(guess)
  if actual_number == com_num:
    print(f"Your guess is right number is {com_num}")
  else:
    print(f"{com_num} is not the correct number")
else:
  print(f"Invalid number")