marks = [11, 21, 33, 54, 79, 90]

#remove an element from the list by using value O(n) ->> where n is the value to be removed
marks.remove(54)
print(marks)

#remove an element from the list by using index O(1)  
marks.pop()
print(marks)

#remove an specific index from the list O(n)  ->> whare n is index of the element to be removed
marks.pop(2)
print(marks)