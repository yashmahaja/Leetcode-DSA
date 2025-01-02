def binarySearch(nums,start,end,target):
    if start > end:
        return -1
    mid = (start + end ) //2
    if nums[mid] == target:
        return mid
    elif nums[mid] > target:
        return binarySearch(nums,start,mid-1,target)
    else:
        return binarySearch(nums, mid+1, end, target)


nums = [-1,0,3,5,9,12]
target = 0
print(binarySearch(nums,0,len(nums)-1,target))