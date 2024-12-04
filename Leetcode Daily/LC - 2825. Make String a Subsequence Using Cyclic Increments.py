"""
You are given two 0-indexed strings str1 and str2.

In an operation, you select a set of indices in str1, and for each index i in the set,
 increment str1[i] to the next character cyclically. That is 'a' becomes 'b', 'b' becomes 'c', and so on, and 'z' becomes 'a'.

Return true if it is possible to make str2 a subsequence of str1 by performing
the operation at most once, and false otherwise.

Note: A subsequence of a string is a new string that is formed from the original string
by deleting some (possibly none) of the characters without disturbing the relative positions of the remaining characters.

"""

def canMakeSubsequence(str1: str, str2: str) -> bool:
    pointer1, pointer2 = 0, 0

    while pointer1 < len(str1) and pointer2 < len(str2):
        current_char = str1[pointer1]
        target_char = str2[pointer2]

        if current_char == target_char or (ord(current_char) - ord("a") + 1) % 26 == (ord(target_char) - ord("a")):
            pointer2 += 1

        pointer1 += 1
    return pointer2 == len(str2)


str1 = "b"
str2 = "c"
print(canMakeSubsequence(str1,str2))


