def max_finder(*nums):
  # If no arguments are passed to the function, return None
  if len(nums) == 0:
    return None
  
  # Initialize max_num with the first number in the collection
  max_num = nums[0]

  # Loop through each number to compare it against the current maximum
  for num in nums:
    # If the current number is larger, update max_num
    if num>max_num:
      max_num = num
  # Return the largest number found    
  return max_num

print(max_finder(10,2,3,12,4,12,34))