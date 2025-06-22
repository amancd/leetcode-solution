class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        ans = []

        l = 0
        for r in range(len(s)):
            if r - l + 1 == k:
                ans.append(s[l:r+1])
                l = r+1
    
        temp = len(ans) * k
        final = len(s) - temp

        print(final)

        l = k - final

        if final !=0:
            word = s[-final:] + (fill * l)
            ans.append(word)

        return ans