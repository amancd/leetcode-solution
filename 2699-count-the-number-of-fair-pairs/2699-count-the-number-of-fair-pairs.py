class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        
        #Optimal
        nums.sort()
        n = len(nums)
        count = 0

        # Upper bound
        for i in range(n-1):
            l = i + 1
            r = n - 1
            while l<=r:
                mid = (l + r)//2

                if nums[i] + nums[mid] >=lower:
                    r = mid - 1
                
                else:
                    l = mid + 1
            
            lower_bound = l

        # Lower bound
            l = i + 1
            r = n - 1
            while l<=r:
                mid = (l + r)//2

                if nums[i] + nums[mid] <=upper:
                    l = mid + 1
                
                else:
                    r = mid - 1
            
            upper_bound = r

            if lower_bound <= upper_bound:
                count += upper_bound - lower_bound + 1
        
        return count

        # Brute 
        # count = 0
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if i>=0 and i<j<len(nums):
        #             if lower <= (nums[i] + nums[j]) <= upper:
        #                 count+=1
        
        # return count