# Last updated: 1/31/2026, 1:40:58 PM
1class Solution:
2    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
3        """
4        Do not return anything, modify nums1 in-place instead.
5        """
6        
7        m = m - 1
8        n = n - 1
9        k = len(nums1) - 1
10
11        while m >= 0 and n >= 0:
12            if nums1[m] > nums2[n]:
13                nums1[k] = nums1[m]
14                m -= 1
15            else:
16                nums1[k] = nums2[n]
17                n -= 1
18            
19            k -= 1
20        
21        while m >= 0 and k >= 0:
22            nums1[k] = nums1[m] 
23            m -= 1
24            k -= 1
25
26        while n >= 0 and k >= 0:
27            nums1[k] = nums2[n]
28            n -= 1
29            k -= 1