class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        print(freq)

        for k, v in freq.items():
            if v == 1:
                return k
            elif v%2!=0:
                return k
        
        return -1