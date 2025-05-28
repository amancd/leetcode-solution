class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        newstr = ""

        for w in s:
            if w.isalnum():
                newstr += w.lower()
        
        print(newstr)

        return newstr == newstr[::-1]