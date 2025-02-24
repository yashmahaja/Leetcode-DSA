from collections import defaultdict


def topKFrequent(nums, k):
    res = defaultdict(int)

    for i in nums:
        res[i] += 1

    ans = sorted(res.keys(), key=lambda x: res[x], reverse=True)

    return ans[:k]

    # hashm = Counter(nums)

    # Step 2: Use a min-heap to get the top k frequent elements
    # return heapq.nlargest(k, hashm.keys(), key=hashm.get)

nums = [1, 1, 1, 2, 2, 3]
k = 2
ans = topKFrequent(nums, k)
print(ans)

root = [3,4,1,2,5]
subRoot = [4,1,2]

print(subRoot in root)
