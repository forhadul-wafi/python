#Tuple containing authorized user info
login_info = (("admin",1234), ("media", 4321))

# Prompt the user for their identification 
user_id = input("Enter your ID: ")
user_pass = int(input("Enter your Pass: ")) #convert the input string to an integer

# Initialize a boolean flag to track if a match is found
found = False

#Unpacking Tuple in loops
for user,password in login_info:
  # Check if both the ID and password match the current record
  if user == user_id and password == user_pass:
    found = True

#Evaluate the flag to determine the output message
if found == True:
  print("Login Successful")
else:
  print("Invalid")
