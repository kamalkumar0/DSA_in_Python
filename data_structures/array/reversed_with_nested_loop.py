#using nested loop to traverse 2D array
data = [[1, 2, 3],#row0
        [4, 5, 6],#row1
        [7, 8, 9] #row2
    ] 

for row in data:
    for mark in range(len(row)- 1, -1, -1):
        print(row[mark], end=" ")
    print()