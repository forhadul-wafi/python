correct_name = "admin"
correct_pass = 1234
std_name = "Wafi"
std_id = "2023-3-60-095"
current_sem = "Spring"

user_name = input("Enter your Id no : ")
user_pass = int(input("Enter your Password : "))

if correct_name == user_name:
    if correct_pass == user_pass:
        print(f"Login successful")
        print("-------------------------")
        print(f"Student Name: {std_name}")
        print(f"Student ID: {std_id}")
        print(f"Semester: {current_sem}")
        print("-------------------------")
        mark = input("Enter your marks: ")
        if mark.isdigit():
            number = int(mark)
            if number >= 80:
                print(f"Result: A+")
            elif number >= 70 and number < 80:
                print(f"Result: A")
            elif number >= 60 and number < 70:
                print(f"Result: A-")
            elif number >= 50 and number < 60:
                print(f"Result: B")
            elif number >= 40 and number < 50:
                print(f"Result: C")
            else:
                print(f"Fail")
    else:
        print(f"Invalid password")
else:
    print(f"Invalid ID")
