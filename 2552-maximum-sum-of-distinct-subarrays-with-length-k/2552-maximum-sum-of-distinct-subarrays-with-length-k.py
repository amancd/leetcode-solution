class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        l=0
        r=k
        total = 0
        res = 0
        seen = set()

        for r in range(n):
            while nums[r] in seen:
                seen.remove(nums[l])
                total -= nums[l]
                l +=1
            
            seen.add(nums[r])
            total += nums[r]

            if r - l + 1 == k:
                res = max(res, total)

                seen.remove(nums[l])
                total -= nums[l]
                l += 1
        
        return res