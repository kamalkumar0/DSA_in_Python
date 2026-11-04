marks = [10, 20, 30, 40, 50]

# #left to right traversal of the list O(n)
# for mark in marks:
#     print(mark, end=" ")

# # 2nd method left to right traversal of the list O(n)
# for i in range(len(marks)):
#     print(marks[i], end=" ")
    
# #right to left traversal of the list O(n)
# for i in range(len(marks)-1, -1, -1):
#     print(marks[i], end=" ")


# Right to left traversal of the list
for mark in reversed(marks):
    print(mark, end=" ")
