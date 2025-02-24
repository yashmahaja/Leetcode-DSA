def search(nums, target):
    left = 0
    right = len(nums) - 1
    while left < right:
        mid = (left + right ) // 2
        if nums[mid] == target:
            return mid
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid
    return left if nums[left] == target else -1


nums = [4,5,6,7,0,1,2]
target = 0
print(search(nums,target))