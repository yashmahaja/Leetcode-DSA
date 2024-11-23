from collections import defaultdict


def topKFrequent(nums, k):
    res = defaultdict(int)
    final = []

    for i in nums:
        res[i] += 1

    ans = sorted(res.keys(), key=lambda x: res[x], reverse=True)
    print(ans)

    for i in range(k):
        final.append(ans[i])

    return final


nums = [1, 1, 1, 2, 2, 3]
k = 2
ans = topKFrequent(nums, k)
print(ans)

root = [3,4,1,2,5]
subRoot = [4,1,2]

print(subRoot in root)
