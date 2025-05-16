class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        pair = {'}':'{', ')':'(', ']':'['}

        for ch in s:
            if ch not in pair:
                stack.append(ch)
            else:
                if not stack or stack[-1] != pair[ch]:
                    return False
                else:
                    stack.pop()

        if len(stack) == 0:
            return True

        return False