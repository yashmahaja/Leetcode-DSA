# Last updated: 2/17/2026, 2:47:03 PM
1class Solution:
2    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
3        if len(nums1) > len(nums2):
4            nums2, nums1 = nums1, nums2
5        
6        m = len(nums1)
7        n = len(nums2)
8        l = 0
9        r = m
10        half = (m + n) // 2
11        while l <= r:
12            mid1 = (l + r) // 2
13            mid2 = half - mid1
14
15            l1 = nums1[mid1 - 1] if mid1 > 0 else float("-inf")
16            l2 = nums2[mid2 - 1] if mid2 > 0 else float("-inf")
17            r1 = nums1[mid1] if  mid1 < len(nums1) else float("inf")
18            r2 = nums2[mid2] if mid2 < len(nums2) else float("inf")
19
20            if l1 <= r2 and l2 <= r1:
21                if (m + n) % 2 == 0:
22                    return (max(l1,l2) + min(r1,r2)) / 2
23                else:
24                    return min(r1,r2)
25
26            if l1 > r2:
27                r = mid1 - 1
28            else:
29                l = mid1 + 1
30        
31        return -1
32
33
34            