def minSubArr(target,nums):
    l = 0
    res = float("inf")
    add = 0
    for r in range(len(nums)):
        add += nums[r]
        while add >= target:
            add -= nums[l]
            res = min(res, r - l + 1)
            l += 1
    return 0 if res == float("inf") else res

nums = [1,2,3,4,5]
target = 11

print(minSubArr(target,nums))

