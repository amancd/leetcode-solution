class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        freq = {}
        freq_sy = {}

        for word in words:
            if len(set(word)) != 1:
                if word not in freq:
                    freq[word] = 1
                else:
                    freq[word] += 1
            else:
                if word not in freq_sy:
                    freq_sy[word] = 1
                else:
                    freq_sy[word] += 1

        count = 0
        used = set()


        for word in freq:
            rev = word[::-1]
            if rev in freq and word not in used and rev not in used:
                pair_count = min(freq[word], freq[rev])
                count += pair_count * 4
                used.add(word)
                used.add(rev)
                

        has_center = False
        for word in freq_sy:
            pair_count = freq_sy[word] // 2
            count += pair_count * 4 
            if freq_sy[word] % 2 == 1 and not has_center:
                count += 2  
                has_center = True

        return count
