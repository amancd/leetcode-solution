class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        pairs = {"}":"{", ")":"(", "]":"["}

        for st in s:
            if st not in pairs:
                stack.append(st)
            
            else:
                if not stack or stack[-1] != pairs[st]:
                    return False

                else:
                    stack.pop()
        
        return True if not stack else False