#List of numbers
numbers = [1,2,3,4,5,6,7,8,9]

#Dictionary to hold the even,odd as key and number's frequency as values
new_dict = {
  #Both key initialized 0
  "even" : 0, 
  "odd" : 0
}

#For loop
for num in numbers:
  #Check if the number is even
  if num % 2 == 0:
    new_dict["even"] += 1
  else:
    new_dict["odd"] += 1
print(new_dict)
