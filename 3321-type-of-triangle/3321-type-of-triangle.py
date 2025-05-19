class Solution:
    def triangleType(self, nums: List[int]) -> str:
        
        if len(set(nums)) == 1:
            return "equilateral"

        x, y, z = nums   

        if (x + y) > z and (x + z) > y and (y+z) > x:
            if len(set(nums)) == 2:
                return "isosceles"
        
        

        if (x + y) > z and (x + z) > y and (y+z) > x:
            return "scalene" 


        return "none"