text = "banana"

#Empty dictionary to hold the output 
empty_dict = {}

#For loop for checking 
for k in text:
  empty_dict[k] = empty_dict.get(k,0) + 1 #If letter already exist then update 

#Output in dictionary
print(empty_dict)