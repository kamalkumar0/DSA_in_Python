def two_pointer(arr, target):
    left = 0
    right = len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]

        if current_sum == target:
            return (arr[left], arr[right])
        
        elif current_sum < target:
            left += 1

        else:
            right -= 1

    return []  # Return an empty list if no pair is found

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 8

result = two_pointer(arr, target)
print(result)  # Output: (1, 9) or (2, 8) or (3, 7) or (4, 6) depending on the implementation