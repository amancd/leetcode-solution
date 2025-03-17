class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        freq = {}

        for n in nums:
            if n not in freq:
                freq[n] = 1
            else:
                freq[n] += 1
        
        print(freq)

        for k, v in freq.items():
            if v%2!=0:
                return False
        
        return True