#List of fruits
fruits = ["apple","mango","pineapple","banana"]

#Empty dictionary to hold final output
emt_dict = {}
for k in fruits:
  emt_dict[k] = len(k) # Finding the length of value

#string is key and len of string is value in dictionary
print(emt_dict)
