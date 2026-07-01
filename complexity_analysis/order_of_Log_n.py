def find_name(name_list, target_name):
    left = 0
    right = len(name_list) - 1

    while left <= right:
        mid = (left + right) // 2
        mid_name = name_list[mid]

        if mid_name == target_name:
            return mid  # Target found at index mid
        elif mid_name < target_name:
            left = mid + 1  # Search in the right half
        else:
            right = mid - 1  # Search in the left half

    return -1  # Target not found

name_list = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Kamal']
target_name = "Kamal"

result_index = find_name(name_list, target_name)
print(f"Index of '{target_name}': {result_index}")
