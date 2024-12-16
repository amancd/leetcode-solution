class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        
        for _ in range(k):

            minimum = min(nums)
            idx = nums.index(minimum)
            nums[idx] = nums[idx] * multiplier

        return nums
