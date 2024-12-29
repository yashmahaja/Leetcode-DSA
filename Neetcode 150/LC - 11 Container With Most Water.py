"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
"""
def maxArea(height):
    right = len(height) - 1
    left = 0
    ans = 0
    while left < right:
        width = right - left
        ans = max(ans, width * min(height[right], height[left]))

        if height[right] < height[left]:
            right -= 1
        else:
            left += 1
    return ans


# height = [1,8,6,2,5,4,8,3,7]
height = [1, 2, 1]
print(maxArea(height))