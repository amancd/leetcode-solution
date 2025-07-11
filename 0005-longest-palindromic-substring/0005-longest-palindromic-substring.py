class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        res = ""
        maximum = 0

        for i in range(len(s)):
            for j in range(i+1):
                st = s[j:i+1]

                if st == st[::-1]:
                    if len(st) > maximum:
                        maximum = len(st)
                        res = st
        
        return res