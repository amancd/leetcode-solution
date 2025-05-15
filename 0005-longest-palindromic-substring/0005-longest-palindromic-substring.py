class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        res = ""
        maximum = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                st = s[i:j+1]

                if st == st[::-1]:
                    if len(st) > maximum:
                        res = st
                        maximum = len(st)
            
        return res
