class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        pairs = {"}":"{", ")":"(", "]":"["}

        for ch in s:
            if ch not in pairs:
                stack.append(ch)

            else:

                if not stack or stack[-1] != pairs[ch]:
                    return False
                else:
                    stack.pop()
        
        return True if not stack else False