students = ["Kamal", "John", "Kamal", "Alice", "Bob", "Alice"]

def clean(students):
    left = 0    

    for right in range(1, len(students)):
        if students[left] != students[right]:
            left += 1
            students[left] = students[right]

    return left + 1

    

print("Original list:", students)
print(clean(students))