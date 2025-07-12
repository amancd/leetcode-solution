class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        minproduct = nums[0]
        maxproduct = nums[0]

        res = nums[0]
        
        for num in nums[1:]:

            if num < 0:
                minproduct, maxproduct = maxproduct, minproduct

            minproduct = min(num, minproduct * num)
            maxproduct = max(num, maxproduct * num)

            res = max(res, maxproduct)
    
        return res