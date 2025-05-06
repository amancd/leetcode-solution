class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        L = []
        for i in range(len(nums)):
            L.append(nums[nums[i]])
        
        return L