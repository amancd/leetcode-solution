class Solution:
    def canChange(self, start: str, target: str) -> bool:
        startarr = []
        targetarr = []
        for i in range(len(start)):
            if start[i]!='_':
                startarr.append(start[i])
            if target[i]!='_':
                targetarr.append(target[i])
            if (target[i] == 'R' and len(startarr)<len(targetarr)) or (start[i] == 'L' and len(startarr)>len(targetarr)):
                return False

        return startarr == targetarr