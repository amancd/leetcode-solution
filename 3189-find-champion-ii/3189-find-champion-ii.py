class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        
        in_degree = [0] * n
        out_degree = [0] * n

        for u, v in edges:
            out_degree[u] += 1
            in_degree[v] += 1
        
        print(in_degree)

        a = in_degree.count(0)

        print(a)

        if a>1:
            return -1

        for i in range(n):
            if in_degree[i] == 0:
                return i
        
        
        return -1
