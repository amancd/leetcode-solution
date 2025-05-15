class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        freq_s = {}
        freq_t = {}

        for ch in s:
            if ch not in freq_s:
                freq_s[ch] = 1
            else:
                freq_s[ch] += 1
        
        for ch in t:
            if ch not in freq_t:
                freq_t[ch] = 1
            else:
                freq_t[ch] += 1

        if freq_s == freq_t:
            return True

        return False