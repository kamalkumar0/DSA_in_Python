def find_duplicate(list):
    seen = set()
    for item in list:
        if item in seen:
            return True
        seen.add(item)
    return False

list_of_students = ["Kamal", "Karan", "Sudarshan", "Satyam", "Karan"]
result = find_duplicate(list_of_students)

if result:
    print("Duplicate found")
else:
    print("Not Found")