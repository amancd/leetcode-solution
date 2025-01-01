class Solution:
    def maxScore(self, s: str) -> int:
        maximum = 0
        for i in range(len(s)-1):
            count_zeros = s[:i+1].count('0')
            count_ones = s[i+1:].count('1')

            total = count_zeros + count_ones

            maximum = max(maximum, total)

        return maximum