class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()
        max_beauty = []
        current_max = 0
        
        for price, beauty in items:
            current_max = max(current_max, beauty)
            max_beauty.append((price, current_max))
        
        print(max_beauty)
        
        def binary_search(q):
            low, high = 0, len(max_beauty) - 1
            while low <= high:
                mid = (low + high) // 2
                if max_beauty[mid][0] <= q:
                    low = mid + 1
                else:
                    high = mid - 1
            return high
        
        result = []
        for q in queries:
            idx = binary_search(q)
            if idx >= 0:
                result.append(max_beauty[idx][1])
            else:
                result.append(0)

        # Brute Force
        # for n in queries:
        #     maximum = 0
        #     for i in range(len(items)):
        #         if items[i][0] <= n:
        #             maximum = max(maximum, items[i][1])
        #         else:
        #             break
            
        #     result.append(maximum)
        
        return result