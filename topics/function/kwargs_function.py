#The **kwargs parameter allows a function to accept any number of keyword arguments.
#Inside the function, kwargs becomes a dictionary containing all the keyword arguments
def my_function(**person):
  print("Name is : ",person["name"])
  print("Age is : ",person["age"])
  print("City is : ",person["city"])

my_function(name="Wafi",age=21,city="Dhaka")

#Combine regular parameters with **kwargs.
def extra_info(country, **person):
  print("Country :",country)
  print("Additional Information: ")
  for key, value in person.items():
    print(" ", key + ":", value)


extra_info("Bangladesh", University = "EWU", hobby = "coding")
