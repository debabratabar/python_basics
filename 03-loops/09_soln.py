items = ["apple", "banana", "orange", "apple", "mango"]

for item in items:
    if items.count(item)>1:
        print(item)
        exit()

print("There is no duplicate item in the list ")