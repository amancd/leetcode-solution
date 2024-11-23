class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        def shift_stones(row):
            n = len(row)
            result = row[:]
            write_index = n - 1
            for i in range(n - 1, -1, -1):
                if row[i] == '*':
                    write_index = i - 1
                elif row[i] == '#':
                    if write_index != i:
                        result[write_index], result[i] = result[i], result[write_index]
                    write_index -= 1            
            return result

        matrix = [shift_stones(row) for row in box]
        rows = len(matrix)
        cols = len(matrix[0])
        transposed = [[None] * rows for _ in range(cols)]

        for i in range(rows):
            for j in range(cols):
               transposed[j][i] = matrix[i][j]
        
        for row in transposed:
            row.reverse()

        return transposed



