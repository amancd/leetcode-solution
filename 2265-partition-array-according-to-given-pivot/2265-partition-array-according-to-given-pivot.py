class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        
        idx = nums.index(pivot)
        lesser = []
        greater = []
        equal = []
        pivots = [pivot]

        for i in range(0, len(nums)):
            if nums[i] < nums[idx]:
                lesser.append(nums[i])
            elif nums[i] > nums[idx]:
                greater.append(nums[i])
            else:
                equal.append(nums[i])
            
        print(lesser)
        print(greater)

        return (lesser + equal + greater)