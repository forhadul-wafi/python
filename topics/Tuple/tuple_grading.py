# Tuple containing student data (name, marks)
students = (("Wafi", 70), ("Rafin", 78), ("Bilal", 90), ("Haris", 99), ("Rifat", 88))

# Initialize variables for calculations
total = 0
top_std = ""  # Name of the student with highest marks
top_marks = 0  # Highest marks found so far

# Iterate through each student using tuple unpacking
for name, marks in students:

    # Add current student's marks to the total
    total += marks

    # Update top scorer if current student has higher marks
    if marks > top_marks:
        top_marks = marks
        top_std = name

# Calculate average marks
avg = total / len(students)

# Output results
print(f"Average marks : {avg}")
print(f"Top Scorer : {top_std} \nObtained Marks : {top_marks}")
