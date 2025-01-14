class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        freq = []
        freq.append([A[0], B[0]])

        ans = [0] * len(A)

        for i in range(1, len(A)):
            freq.append(freq[i - 1] + [A[i], B[i]])

        print(freq)

        for i, lst in enumerate(freq):
            count = 0
            for x in set(lst):
                if lst.count(x) > 1: 
                    count += 1
            ans[i] = count

        return ans