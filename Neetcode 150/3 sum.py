
def threeSum(nums):
    nums.sort()
    n = len(nums)
    ans = []
    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        j = i + 1
        k = n - 1
        while j < k:
            if nums[i] + nums[j] + nums[k] < 0:
                j += 1
            elif nums[i] + nums[j] + nums[k] > 0:
                k -= 1
            else:
                ans.append([nums[i], nums[j], nums[k]])

                while j < k and nums[j] == nums[j + 1]:
                    j += 1
                while j < k and nums[k] == nums[k - 1]:
                    k -= 1

                j += 1
                k -= 1
    return ans


nums =[1, -1, -1, 0]
print(threeSum(nums))