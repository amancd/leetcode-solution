class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:

        def isPrefixAndSuffix(a, b):
            w1 = len(a)
            w2 = len(b)

            if w1<=w2:
                if a in b[:w1] and a in b[-w1:]:
                    return True
        
            return False
        
        count = 0
        for i in range(len(words)):
            for j in range(len(words)):
                if i<j and isPrefixAndSuffix(words[i], words[j]):
                    count+=1
        
        return count