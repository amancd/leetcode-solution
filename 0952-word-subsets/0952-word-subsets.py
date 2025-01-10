class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        def check_freq(word):
            freq = {}
            for w in word:
                if w not in freq:
                    freq[w] = 1
                else:
                    freq[w] += 1
            return freq
        
        max_freq = {}
        for w in words2:
            freq = check_freq(w)
            for k in freq:
                if k in max_freq:
                    max_freq[k] = max(max_freq[k], freq[k])
                else:
                    max_freq[k] = freq[k]
            
        
        print(max_freq)

        ans = []
        for w in words1:
            freq2 = check_freq(w)
            valid = True
            for k, v in max_freq.items():
                if freq2.get(k, 0) < v:
                    valid = False
            
            if valid:
                ans.append(w)


        return ans