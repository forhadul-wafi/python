words = ["apple", "banana", "apple", "orange", "apple", "apple", "orange", "orange"]

count = {}

for word in words:
    count[word] = count.get(word, 0) + 1

print(count)