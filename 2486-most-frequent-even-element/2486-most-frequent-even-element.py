class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        freq = {}

        nums.sort()
        for n in nums:
            if n%2==0:
                if n not in freq:
                    freq[n] = 1
                else:
                    freq[n] += 1
            
        print(freq)
        
        maximum = -1
        for k, v in freq.items():
            maximum = max(maximum, v)

        print(maximum)
        
        for k, v in freq.items():
            if v == maximum:
                return k
        
        return -1