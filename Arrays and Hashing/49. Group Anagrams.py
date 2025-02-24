from collections import defaultdict


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


# Second method O(nlogn) Time Complexity
#     anagram_map = defaultdict(list)
#
#     for word in strs:
#         sorted_words = ''.join(sorted(word))
#         anagram_map[sorted_words].append(word)
#
#     return list(anagram_map.values())

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
result = groupAnagrams(strs)
print(result)



