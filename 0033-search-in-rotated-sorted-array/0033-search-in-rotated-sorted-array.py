class Solution:
    def search(self, nums: List[int], target: int) -> int:

        try:
            idx = nums.index(target)
            return idx
        except:
            return -1