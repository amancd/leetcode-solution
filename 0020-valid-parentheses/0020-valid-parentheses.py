class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        
        pair = {")": "(", "}": "{", "]": "["}
        stack = []

        for ch in s:
            if ch in pair:  # If it's a closing bracket
                if len(stack) == 0 or stack[-1] != pair[ch]:
                    return False
                stack.pop()
            else:  # If it's an opening bracket
                stack.append(ch)
        
        # If the stack is empty, all brackets are matched
        return len(stack) == 0
