marks = [11, 21, 33, 54, 79, 90]

#remove an element from the list by using value O(n)
marks.remove(54)
print(marks)

#remove an element from the list by using index O(1)  
marks.pop()
print(marks)

#remove an specific index from the list O(n)   
marks.pop(2)
print(marks)