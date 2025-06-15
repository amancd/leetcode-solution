class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        res = ""
        maximum = 0

        for i in range(len(s)):
            for j in range(i+1):
                if s[j:i+1] == s[j:i+1][::-1]:
                    if len(s[j:i+1]) > maximum:
                        res = s[j:i+1]
                        maximum = len(s[j:i+1])
        
        return res