class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        maximum = 0


        for i in range(len(s)):
            for j in range(i, len(s)):
                if len(set(s[i:j+1])) == len(s[i:j+1]):
                    maximum = max(maximum, j - i + 1)
                else:
                    break
        
        return maximum
