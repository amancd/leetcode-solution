class Solution:
    def smallestNumber(self, pattern: str) -> str:
        stack = []
        ans = []
        num = 1  
        
        for i in range(len(pattern) + 1):  

            stack.append(num)
            num += 1 
            
            if i == len(pattern) or pattern[i] == 'I':  
                while stack:
                    ans.append(str(stack.pop()))
        
        return "".join(ans)
