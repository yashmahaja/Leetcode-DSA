from collections import defaultdict
from typing import List


def groupAnagrams(strs):
    res = {}

    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1

        count = tuple(count)
        if count not in res:
            res[count] = []

        res[count].append(s)

    return list(res.values())

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
result = groupAnagrams(strs)
print(result)