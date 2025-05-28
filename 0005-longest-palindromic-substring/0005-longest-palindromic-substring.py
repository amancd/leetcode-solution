class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        res = ""
        maximum = 0

        for i in range(len(s)):
            for j in range(i, len(s)):
                st = s[i:j+1]

                if st[::-1] == st:
                    if maximum < len(st):
                        maximum = len(st)
                        res = st
        
        return res