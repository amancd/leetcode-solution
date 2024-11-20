class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        total_count = Counter(s)
        if total_count['a'] < k or total_count['b'] < k or total_count['c'] < k:
            return -1
        
        n = len(s)
        left_count = Counter({'a': 0, 'b': 0, 'c': 0})
        max_valid_length = 0
        start = 0

        for end in range(n):
            left_count[s[end]] += 1

            while (
                total_count['a'] - left_count['a'] < k or
                total_count['b'] - left_count['b'] < k or
                total_count['c'] - left_count['c'] < k
            ):
                left_count[s[start]] -= 1
                start += 1

            max_valid_length = max(max_valid_length, end - start + 1)

        return n - max_valid_length