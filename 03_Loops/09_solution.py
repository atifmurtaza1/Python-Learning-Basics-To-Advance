items = ["apple", "banana", "orange", "apple", "mango",]
item_duplicate = set()

for item in items:
    if(item in item_duplicate):
        print("duplicate: ", item)
    else:
        item_duplicate.add(item)
    