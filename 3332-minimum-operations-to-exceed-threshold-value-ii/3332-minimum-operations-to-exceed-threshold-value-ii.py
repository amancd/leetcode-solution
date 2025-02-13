class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        
        heapq.heapify(nums)

        def fn(arr):
            for n in arr:
                if n<k:
                    return True
            
            return False


        count = 0
        while fn(nums):
            min1 = heapq.heappop(nums)
            min2 = heapq.heappop(nums)

            print(min1)

            element = min(min1, min2) * 2 + max(min1, min2)

            nums.append(element)
            count+=1
        
        return count