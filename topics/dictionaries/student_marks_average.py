#Dictionary & list as values
marks = {
    "Rahim": [80, 90, 70],
    "Karim": [60, 75, 65]
}

#Empty dictionary to hold the output
avg = {}

#Loop through both keys & values
for name, mark in marks.items():
    avg[name] = round(sum(mark)/len(mark),2) #Rounded the floating value upto 2 digit
print(avg)

    