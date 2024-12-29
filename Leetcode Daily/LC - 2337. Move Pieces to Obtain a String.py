"""
You are given two strings start and target, both of length n.
Each string consists only of the characters 'L', 'R', and '_' where:

The characters 'L' and 'R' represent pieces, where a piece 'L' can move
to the left only if there is a blank space directly to its left, and a
 piece 'R' can move to the right only if there is a blank space directly to its right.
The character '_' represents a blank space that can be occupied by any of the 'L' or 'R' pieces.
Return true if it is possible to obtain the string target by moving the
 pieces of the string start any number of times. Otherwise, return false.

"""

def canChange(start: str, target: str) -> bool:
    if start.replace('_', '') != target.replace('_', ''):
        return False

    pointer1, pointer2 = 0, 0
    n = len(start)

    while pointer1 < n and pointer2 < n:
        while pointer1 < n and start[pointer1] == '_':
            pointer1 += 1
        while pointer2 < n and target[pointer2] == '_':
            pointer2 += 1


        if pointer1 == n and pointer2 == n:
            return True

        if (pointer1 == n) != (pointer2 == n):
            return False

        if start[pointer1] != target[pointer2]:
            return False


        if start[pointer1] == 'L' and pointer1 < pointer2:
            return False
        if start[pointer1] == 'R' and pointer1 > pointer2:
            return False

        pointer1 += 1
        pointer2 += 1

    return True



start = "_L__R__R_"
target = "L______RR"
ans = canChange(start, target)
print(ans)
