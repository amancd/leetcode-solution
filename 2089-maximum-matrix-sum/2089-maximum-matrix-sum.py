class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:

        result = 0
        rows = len(matrix)
        cols = len(matrix[0])

        minimum = abs(matrix[0][0])

        negative = 0

        for i in range(rows):
            for j in range(cols):
                result += abs(matrix[i][j])
                if matrix[i][j] < 0:
                    negative += 1
                
                minimum = min(minimum, abs(matrix[i][j]))
        
        print(abs(0))
        print(minimum)
        
        if negative % 2 == 0:
            return result
        
        else:
            return result - (2 * minimum)

        return 4