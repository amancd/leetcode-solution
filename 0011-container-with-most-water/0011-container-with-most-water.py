class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        l = 0
        r = len(height) - 1
        maximum = 0

        while l < r:
            h = min(height[l], height[r])
            w = r - l
            area = h * w

            maximum = max(maximum, area)

            if height[l] < height[r]:
                l+=1
            else:
                r-=1
        
        return maximum