class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        ans = []
        minimum = float('inf')
        
        for word in strs:
            minimum = min(minimum, len(word))
        
        j = 0
        while j < minimum:
            char = strs[0][j]
            
            for i in range(1, len(strs)):
                if strs[i][j] != char:
                    return "".join(ans)
            
            ans.append(char)
            j += 1 
        
        return "".join(ans)
