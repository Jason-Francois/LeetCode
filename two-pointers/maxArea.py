# Container with most water

class Solution(object):
    # Time Complexity: O(n), iterate through array once
    # Space Complexity: O(1), no extra DS used
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l,r = 0, (len (height) - 1)
        maxAreaOfWater = 0
        while (l < r):
            maxAreaOfWater = max(maxAreaOfWater, min(height[l], height[r]) * (r - l))
            if height[l] < height[r]:
                l+=1
            else:
                r-=1
            
        return maxAreaOfWater