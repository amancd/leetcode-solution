class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:

        right = max(nums)
        left = 1

        while left < right:
            mid = (left + right)//2
            total = 0
            for num in nums:
                total += (num - 1) // mid

            if total <=maxOperations:
                right = mid
            else:
                left = mid + 1
        
        return left


