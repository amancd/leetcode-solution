class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        l = 0
        r = len(height) - 1
        maximum_area = 0

        while l < r:
            w = r - l
            h = min(height[l], height[r])
            maximum_area = max(maximum_area, w * h)

            if height[l] < height[r]:
                l+=1
            else:
                r-=1
        
        return maximum_area