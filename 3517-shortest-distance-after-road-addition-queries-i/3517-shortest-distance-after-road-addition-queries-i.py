class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)
        for i in range(n - 1):
            graph[i].append(i + 1)

        print(graph)

        def bfs(start, target):
            queue = deque([start])
            visited = [-1] * n
            visited[start] = 0

            print(visited)

            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if visited[neighbor] == -1:  # not visited
                        visited[neighbor] = visited[node] + 1
                        queue.append(neighbor)
                        if neighbor == target:
                            return visited[neighbor]
            return -1 

        result = []
        for ui, vi in queries:
            graph[ui].append(vi)
            shortest = bfs(0, n - 1)
            result.append(shortest)

        return result