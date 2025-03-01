class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        

        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[i+1]:
                    nums[i] = nums[i] * 2
                    nums[i+1] = 0
        
        zero = nums.count(0)

        counts = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                nums.remove(0)
                nums.append(0)
                counts+=1

            if counts == zero:
                break
        

        return nums