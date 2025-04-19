class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        n = len(nums)
        count = 0
        for i in range(n):
            l = i + 1
            r = n - 1

            while l <= r and nums[l] + nums[i] < lower:
                l += 1

            while r >= l and nums[r] + nums[i] > upper:
                r -= 1

            count += max(0, r - l + 1)

        return count
