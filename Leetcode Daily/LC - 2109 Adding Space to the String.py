
"""
You are given a 0-indexed string s and a 0-indexed integer array spaces that describes
the indices in the original string where spaces will be added. Each space should be inserted before
the character at the given index.

For example, given s = "EnjoyYourCoffee" and spaces = [5, 9], we place spaces before
'Y' and 'C', which are at indices 5 and 9 respectively. Thus, we obtain "Enjoy Your Coffee".
Return the modified string after the spaces have been added.

"""
def addSpaces(s, spaces):
    # ans = []
    # pointer = 0
    # for space in spaces:
    #         ans.append(s[pointer:space])
    #         pointer = space
    # ans.append(s[pointer:])
    # ans = " ".join(ans)
    # return ans

    i, j = 0, 0
    res = []

    while i < len(s) and j < len(spaces):
        if i < spaces[j]:
            res.append(s[i])
            i += 1
        else:
            res.append(" ")
            j += 1

    if i < len(s):
        res.append(s[i:])
    return "".join(res)

s = "LeetcodeHelpsMeLearn"
spaces = [8,13,15]
print(addSpaces(s,spaces))
