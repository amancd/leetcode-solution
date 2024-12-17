class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        freq = Counter(s)

        heap = [(-ord(char), count) for char, count in freq.items()]
        heapq.heapify(heap)
        
        res = []
        
        while heap:
            char_neg, count = heapq.heappop(heap)
            char = chr(-char_neg)
            
            append_count = min(count, repeatLimit)
            res.append(char * append_count)
            
            count -= append_count
            
            if count > 0:
                if not heap:
                    break  
            
                next_char_neg, next_count = heapq.heappop(heap)
                next_char = chr(-next_char_neg)
                
                res.append(next_char) 
                next_count -= 1 
                
                if next_count > 0:
                    heapq.heappush(heap, (-ord(next_char), next_count))
                
                heapq.heappush(heap, (-ord(char), count))
        
        return "".join(res)
