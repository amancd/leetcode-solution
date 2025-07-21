class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r  = len(height) - 1
        
        maximum_area = 0
        while l < r:
            h = min(height[l], height[r])
            w = r - l
            area = h * w
            print(area)
            print(type(area))
            maximum_area = max(maximum_area, area)

            if height[l] > height[r]:
                r-=1
            else:
                l+=1
        
        return maximum_area


        