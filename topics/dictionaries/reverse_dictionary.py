#Data dictionary
data = {
    "a": 1,
    "b": 2,
    "c": 3
}

#Empty dictionary
result = {}

#Loop for reverse
for key, value in data.items():
  result[value] = key
print(result)