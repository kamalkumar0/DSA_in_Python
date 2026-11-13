# same direction two pointer problem
# duplicate bhi hat jayenge result me 
students = ["Kamal", "John", "Kamal", "Alice", "Bob", "Alice"]
students.sort()  # Sort the list to group duplicates together

def clean(students):
    left = 0    

    for right in range(1, len(students)):
        if students[left] != students[right]:
            left += 1
            students[left] = students[right]

    return left + 1

count = clean(students)
print("Number of unique students:", count)
print("Unique students:", students[:count])




