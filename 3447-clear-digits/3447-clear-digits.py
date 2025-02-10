class Solution:
    def clearDigits(self, s: str) -> str:
        ans = []

        for ch in s:
            if ch.isalpha():
                ans.append(ch)
            else:
                ans.pop()
        
        return "".join(ans)