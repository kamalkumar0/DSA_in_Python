def add_item(element, list=[]):
    list.append(element)
    return list

a1 = add_item(10)
a2 = add_item(20)

print(f" List A: {a1}")  # Output: [10, 20]
print(f" List B: {a2}")  # Output: [10, 20]