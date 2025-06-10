class Solution:
    def maxDifference(self, s: str) -> int:
        
        freq = {}

        for ch in s:
            if ch not in freq:
                freq[ch] = 1
            else:
                freq[ch] += 1
        
        print(freq)

        maximum = float('-inf')
        minimum = float('inf')

        for k, v in freq.items():
            if v%2!=0:
                maximum = max(maximum, v)
            else:
                if minimum > v:
                    minimum = min(minimum, v)
            
        
        return (maximum - minimum)