data = (1,2,3,4,1,2,2,2,4,7,7,7,8,9,0,1,2,2,6,6,3,4,5)

for item in set(data):
  print(f"{item} : {data.count(item)}")