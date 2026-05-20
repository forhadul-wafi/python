#Nested Dictionary 
students = {
    "Wafi": {
        "math": 80,
        "english": 70
    },
    "Nayeem": {
        "math": 90,
        "english": 85
    }
}
#Outer loop: Iterate through each student
#.items() gives both the key (student name) & value (subjects dictionary)
for name, subjects in students.items():
    # Inner loop: Iterate through each subject's marks for the current student
    for subject, marks in subjects.items():
        print(f"{name} got {marks} in {subject}")
        

