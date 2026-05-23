def calculation(*nums):
  total = 0
  for num in nums:
    total += num
  return total

print("Total is:",calculation(10,10))