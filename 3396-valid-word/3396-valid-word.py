class Solution:
    def isValid(self, word: str) -> bool:
        
        vowels = {'a', 'e', 'i', 'o', 'u'}

        c1 = 0
        c2 = 0
        if word.isalnum():
            for ch in word:
                if ch.lower() not in vowels and ch.isalpha():
                    c2 = 1
                if ch.lower() in vowels:
                    c1 = 1

            
            if len(word) >= 3 and c1 == 1 and c2 == 1:
                return True
            
        return False