#The *args parameter allows a function to accept any number of positional arguments
def total_number(*nums):
  #Always return tuple
  print(type(nums))
  return sum(nums)

print(total_number(1,2,3,4,5))

#Combine regular parameters with *args.
#Regular parameters must come before *arg
def my_function(greeting, *names):
  for name in names:
    print(greeting, name)

my_function("Hello", "Emil", "Tobias", "Linus")


