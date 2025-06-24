class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        
        ans = set()
        for i in range(len(nums)):
            for j in range(len(nums)):
                if abs(i-j) <= k and nums[j] == key:
                    ans.add(i)
        

        return list(ans)