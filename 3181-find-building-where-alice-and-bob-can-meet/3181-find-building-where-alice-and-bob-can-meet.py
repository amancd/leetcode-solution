import heapq

class Solution:
    def leftmostBuildingQueries(self, heights, queries):
        store_queries = [[] for _ in range(len(heights))]
        max_index = []
        result = [-1] * len(queries)

        # Store the mappings for all queries in store_queries.
        for curr_query, query in enumerate(queries):
            a, b = query
            if a < b and heights[a] < heights[b]:
                result[curr_query] = b
            elif a > b and heights[a] > heights[b]:
                result[curr_query] = a
            elif a == b:
                result[curr_query] = a
            else:
                store_queries[max(a, b)].append((max(heights[a], heights[b]), curr_query))

        for index in range(len(heights)):
            # If the priority queue's minimum pair value is less than the current index of height, it is an answer to the query.
            while max_index and max_index[0][0] < heights[index]:
                result[max_index[0][1]] = index
                heapq.heappop(max_index)

            # Push the queries with their maximum index as the current index in the priority queue.
            for element in store_queries[index]:
                heapq.heappush(max_index, element)

        return result