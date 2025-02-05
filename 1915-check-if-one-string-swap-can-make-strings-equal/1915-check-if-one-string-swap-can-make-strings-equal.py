class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        a = Counter(s1)
        b = Counter(s2)

        if s1 == s2:
            return True

        if a!=b:
            return False
        else:
            count = 0
            i=0
            while i<len(s1):
                if s1[i] == s2[i]:
                    count+=1
                i+=1
            
        if len(s2) - count > 2:
            return False
        else:
            return True