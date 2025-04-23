class Solution:
    def countLargestGroup(self, n: int) -> int:

        def sum_of_digits(n):
            total = 0
            while n > 0:
                total += n % 10
                n //= 10
            return total

        freq = {}
        for i in range(1, n+1):
            digit = sum_of_digits(i)

            if digit in freq:
                freq[digit].append([i])
            else:
                freq[digit] = [i]
        
        maximum = 0
        for v in freq.values():
            maximum = max(len(v), maximum)

        print(maximum)

        count = 0
        for v in freq.values():
            if len(v) == maximum:
                count += 1

        return count