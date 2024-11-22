class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:

        freq = defaultdict(int)

        for row in matrix:
            print(row[0])
            if row[0] == 0:
                freq[tuple(row)] += 1
            else:
                freq[tuple([x ^ 1 for x in row])] += 1
        
        print(freq)

        return max(freq.values())