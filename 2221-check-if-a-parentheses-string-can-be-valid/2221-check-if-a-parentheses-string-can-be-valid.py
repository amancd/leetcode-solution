class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 != 0:
            return False
        
        balance = 0
        unlocked = 0 
        for i in range(len(s)):
            if locked[i] == '0':
                unlocked += 1
            elif s[i] == '(':
                balance += 1
            elif balance > 0:
                balance -= 1
            elif unlocked > 0:
                unlocked -= 1
            else:
                return False
        
        balance = 0
        unlocked = 0
        for i in range(len(s) - 1, -1, -1): 
            if locked[i] == '0':
                unlocked += 1
            elif s[i] == ')':
                balance += 1
            elif balance > 0: 
                balance -= 1
            elif unlocked > 0:
                unlocked -= 1
            else:
                return False
        
        return True
