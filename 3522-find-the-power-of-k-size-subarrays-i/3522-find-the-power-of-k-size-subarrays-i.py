class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:

        n = len(nums)
        left = 0
        right = k-1

        result = []
        while left <= n-k and right < n:

            i = left
            is_consecutive = True
            while i<right:
                if nums[i+1] - nums[i] != 1:
                    result.append(-1)
                    is_consecutive = False
                    break
                i+=1
                
            if is_consecutive:
                result.append(nums[right])
            left+=1
            right+=1
        
        return result
