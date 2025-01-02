"""
You are given an m x n 2-D integer array matrix and an integer target.

Each row in matrix is sorted in non-decreasing order.
The first integer of every row is greater than the last integer of the previous row.

"""


def search2Dmatrix(matrix,target):
    if not matrix or not matrix[0]:
        return False

    m = len(matrix)
    n = len(matrix[0])
    left = 0
    right = m * n - 1

    while left <= right:
        mid = (left + right) // 2
        mid_value = matrix[mid // 2][mid % 2]
        if mid_value == target:
            return (mid // 2,mid % 2)
        elif mid_value > target:
            right = mid - 1
        else:
            left = mid + 1



matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]]
target = 10
print(search2Dmatrix(matrix,target))


