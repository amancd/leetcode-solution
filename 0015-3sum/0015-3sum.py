class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        nums.sort()


        for i in range(len(nums)-2):
            
            l = i+1
            r = len(nums) - 1
            
            if nums[i] == nums[i-1]:
                continue
            
            while l < r:

                if nums[i] + nums[l] + nums[r] == 0:
                    res.append([nums[i], nums[l], nums[r]])

                while l<r and nums[l] == nums[l+1]:
                    l+=1
                
                while l<r and nums[r] == nums[r-1]:
                    r-=1

            
            if nums[i] + nums[l] + nums[r] < 0:
                l+=1
            else:
                r-=1
            
        
        return res