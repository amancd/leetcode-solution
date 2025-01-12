class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2!=0:
            return False
        
        pair = {")":"(", "}":"{", "]":"["}
        stack = []

        for ch in s:
            if ch in pair:
                if len(stack) == 0 or stack[-1] != pair[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)

        
        return len(stack) == 0

