class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        total = Counter(s)
        if total['a'] < k or total['b'] < k or total['c'] < k:
            return -1
        
        n = len(s)
        count = Counter({'a':0, 'b':0, 'c':0})
        length = 0
        left = 0

        for right in range(n):
            count[s[right]] += 1

            while( total['a'] - count['a'] < k or total['b'] - count['b'] < k or total['c'] - count['c'] < k):
                count[s[left]] -= 1
                left += 1

            
            length = max(length, right-left + 1)

        return n - length
