class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        maximum = 0
        
        for i in range(n):
            for j in range(i, n):
                substr = s[i:j+1] 
                if len(set(substr)) == len(substr):
                    maximum = max(maximum, j - i + 1)
                else:
                    break

        return maximum
