class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        
        ans = []
        for i in range(len(nums)-2):
            ans.append(nums[i:i+3])

        print(ans)

        count = 0
        for num in ans:
            x, y, z = num
            if 2 * (x + z) == y:
                count+=1


        return count