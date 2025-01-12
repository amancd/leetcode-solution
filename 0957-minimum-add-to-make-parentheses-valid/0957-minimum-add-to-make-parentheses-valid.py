class Solution:
    def minAddToMakeValid(self, s: str) -> int:

        pair = {")":"(", "}":"{", "]":"["}
        opening = 0
        closing = 0
        stack = []
        
        for ch in s:
            if ch in pair:
                if len(stack) != 0 and stack[-1] == pair[ch]:
                        stack.pop()
                else:
                    stack.append(ch)
                print(stack)
            else:
                stack.append(ch)
                print(stack)
        
        # for ch in stack:
        #     if ch in pair:
        #         closing+=1
        #     else:
        #         opening+=1
        
        return len(stack)