class Solution:
    def maximumLength(self, s: str) -> int:
        freq = {}
        n = len(s)
        for i in range(n):
            for j in range(n):
                if len(set(s[i:j+1])) == 1:
                    if s[i:j+1] not in freq:
                        freq[s[i:j+1]] = 1
                    else:
                        freq[s[i:j+1]] += 1

        maximum = -1
        for k, v in freq.items():
            if v>=3:
                maximum = max(len(k), maximum)
        
        return maximum