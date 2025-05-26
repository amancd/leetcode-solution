class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        freq_s = {}
        freq_t = {}

        for ch in s:
            freq_s[ch] = freq_s.get(ch, 0) + 1
        
        for ch in t:
            freq_t[ch] = freq_t.get(ch, 0) + 1
            

        if freq_s == freq_t:
            return True

        return False