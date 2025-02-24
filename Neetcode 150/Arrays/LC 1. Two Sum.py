from black.trans import defaultdict



def twoSum(nums, target):
    # 1st approach o(n^2) TC loop over twice and check if sum == target
    # 2nd approach
    # duplicate = nums.copy()
    # nums.sort()
    # start = 0
    # end = len(nums) - 1
    # lis = []
    # a = 0
    # b = 0
    # while start <= end:
    #     sum = nums[start] + nums[end]
    #     if target == sum:
    #         a = nums[start]
    #         b = nums[end]
    #         break
    #     elif target < sum:
    #         end -= 1
    #     elif target > sum:
    #         start += 1
    # for i in range(len(duplicate)):
    #     if duplicate[i] == a or duplicate[i] == b:
    #         lis.append(i)
    # return lis

    # Third approach T.C O(n) S.C O(n)
    hashmap = defaultdict(int)
    for i,n in enumerate(nums):
        diff = target - n
        if diff in hashmap:
            return [hashmap[diff],i]
        hashmap[n] = i


nums = [2,7,11,15]
target = 9
print(twoSum(nums, target))
