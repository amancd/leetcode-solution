class Solution:
    def decrypt(self, code, k):
        n = len(code)
        result = []

        for left in range(1, n + 1):
            total = 0

            if k > 0:  # Forward traversal
                for right in range(k):
                    idx = (left + right) % n
                    total += code[idx]
                result.append(total)

            elif k < 0:  # Backward traversal
                for right in range(1, abs(k)+1):
                    idx = (left - 1 - right + n) % n  # Correct backward index
                    total += code[idx]
                result.append(total)

            else:  # k == 0, all zeros
                return [0] * n

        return result
