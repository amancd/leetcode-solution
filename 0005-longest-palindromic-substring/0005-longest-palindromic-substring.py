class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        res = ""
        maximum = 0

        for i in range(len(s)):
            for j in range(i, len(s)):
                 if s[i:j+1] == s[i:j+1][::-1]:
                    if maximum < len(s[i:j+1]):
                        res = s[i:j+1]
                        maximum = len(s[i:j+1])
        
        return res