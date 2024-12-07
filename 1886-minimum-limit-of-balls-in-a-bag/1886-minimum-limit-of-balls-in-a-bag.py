class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:

        right = max(nums)
        left = 1

        while left < right:
            mid = (left + right)//2
            total = 0
            for num in nums:
                total += math.ceil(num / mid) - 1

            if total <=maxOperations:
                right = mid
            else:
                left = mid + 1
        
        return left


