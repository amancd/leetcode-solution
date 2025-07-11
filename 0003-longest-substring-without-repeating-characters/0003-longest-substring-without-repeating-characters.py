class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l = 0
        maximum = 0

        for r in range(len(s)):
            if len(set(s[l:r+1])) == len(s[l:r+1]):
                maximum = max(maximum, r - l + 1)
                r += 1
            else:
                l += 1
        
        return maximum