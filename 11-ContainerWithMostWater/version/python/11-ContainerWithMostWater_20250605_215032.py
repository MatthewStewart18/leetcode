# Last updated: 05/06/2025, 21:50:32
class Solution:
    def maxArea(self, height: List[int]) -> int:

        l = 0
        r = len(height) - 1
        res = 0

        while(l < r):
            min_height = min(height[l], height[r])
            currentsum = (r - l) * min_height
            if currentsum > res:
                res = currentsum
            
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return res
        