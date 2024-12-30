"""
You are given an integer array nums and an integer k. Find the maximum subarray sum of all the subarrays of nums that meet the following conditions:

The length of the subarray is k, and
All the elements of the subarray are distinct.
Return the maximum subarray sum of all the subarrays that meet the conditions. If no subarray meets the conditions, return 0.

A subarray is a contiguous non-empty sequence of elements within an array.
"""


def maximumSubarraySum(nums,k):
    i = 0
    j = 0
    sum = 0
    suma = 0
    for pointer in range(k):
        j += 1
        sum += nums[pointer]
    suma = sum
    for point in range(j,len(nums)):
        sum -= nums[i]
        i += 1
        sum += nums[point]
        suma = max(suma,sum)

    return suma
nums = [1,5,4,2,3,1,1]
k = 3
ans = maximumSubarraySum(nums,k)
print(ans)