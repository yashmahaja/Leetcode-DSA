"""
You are given an n x n integer matrix. You can do the following operation any number of times:

Choose any two adjacent elements of matrix and multiply each of them by -1.
Two elements are considered adjacent if and only if they share a border.

Your goal is to maximize the summation of the matrix's elements. Return the maximum sum of
the matrix's elements using the operation mentioned above.

"""


def maxMatrixSum(matrix) -> int:
    add = 0
    matrixmin = float("inf")
    n = 0
    for i in matrix:
        for j in i:
            add += abs(j)
            matrixmin = min(matrixmin, abs(j))
            if j < 0:
                n += 1
    if n & 1:
        add -= 2 * matrixmin

    return add


print(maxMatrixSum([[1,2,3],[-1,-2,-3],[1,2,3]]))