class Solution:
    def findScore(self, nums: List[int]) -> int:
        n = len(nums)
        marked = set()
        score = 0

        indexed_nums = sorted((num, i) for i, num in enumerate(nums))

        for value, idx in indexed_nums:
            if idx not in marked:
                score += value
                marked.add(idx)
                if idx > 0:
                    marked.add(idx - 1)
                if idx < n - 1:
                    marked.add(idx + 1)

        return score
