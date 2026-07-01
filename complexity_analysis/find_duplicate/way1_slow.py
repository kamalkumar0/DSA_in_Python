def find_duplicate(list):
    for i in range(len(list)):
        for j in range(len(list)):
            if i != j and list[i] == list[j]:
                return True
    return False

list_of_students = ["Kamal", "Karan", "Sudarshan", "Satyam", "Karan"]
result = find_duplicate(list_of_students)

if result:
    print("Duplicate found")
else:
    print("Not Found")
    