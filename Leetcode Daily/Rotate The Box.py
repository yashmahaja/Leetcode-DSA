"""
You are given an m x n matrix of characters box representing a side-view of a box. Each cell of the box
is one of the following:

A stone '#'
A stationary obstacle '*'
Empty '.'

The box is rotated 90 degrees clockwise, causing some of the stones to fall due to gravity.
Each stone falls down until it lands on an obstacle, another stone, or the bottom of the box.
Gravity does not affect the obstacles' positions, and the inertia from the box's rotation does
not affect the stones' horizontal positions.
"""

def rotateTheBox(box):
    row, col = len(box), len(box[0])
    for r in range(row):
        i = col - 1
        for c in reversed(range(col)):
            if box[r][c] == "#":
                box[r][c], box[r][i] = box[r][i], box[r][c]
                i -= 1
            elif box[r][c] == "*":
                i = c - 1
    res = []
    for c in range(col):
        column = []
        for r in reversed(range(row)):
            column.append(box[r][c])
        res.append(column)

    return res




box = [["#","#","*",".","*","."],["#","#","#","*",".","."],["#","#","#",".","#","."]]
rotated_box = rotateTheBox(box)
for row in rotated_box:
    print(row)

a = [2,4,5,6,7]
for i, num in enumerate(a):
    print(i,num)

# a.pop(2)
# print(a)