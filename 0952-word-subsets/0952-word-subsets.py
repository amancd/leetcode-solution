class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        max_freq = {}
        for word in words2:
            freq = {}
            for char in word:
                if char in freq:
                    freq[char] += 1
                else:
                    freq[char] = 1
            for char, count in freq.items():
                if char in max_freq:
                    max_freq[char] = max(max_freq[char], count)
                else:
                    max_freq[char] = count

        result = []
        for word in words1:
            freq = {}
            for char in word:
                if char in freq:
                    freq[char] += 1
                else:
                    freq[char] = 1
            
            valid = True
            for char, count in max_freq.items():
                if char not in freq or freq[char] < count:
                    valid = False
                    break
            if valid:
                result.append(word)

        return result
