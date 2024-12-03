class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = ""
        it = 0

        for i in range(len(spaces)):
            res += s[it: spaces[i]]
            res += " "

            it = spaces[i]
            
        res += s[it:]
        return res