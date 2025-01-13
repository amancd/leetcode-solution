class Solution:
    def minimumLength(self, s: str) -> int:
        def frequency(s):
            freq = {}

            for ch in s:
                if ch not in freq:
                    freq[ch] = 1
                else:
                    freq[ch] += 1
            
            return freq

        freq = frequency(s)

        count = 0
        for k, v in freq.items():
            while v>=3:
                count+=2
                v = v - 2
                

        return len(s) - count