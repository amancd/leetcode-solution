class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minproduct = nums[0]
        maxproduct = nums[0]
        result = nums[0]

        for num in nums[1:]:

            if num<0:
                minproduct, maxproduct = maxproduct, minproduct

            maxproduct = max(num, maxproduct * num)
            minproduct = min(num, minproduct * num)

            result = max(result, maxproduct)

        return result