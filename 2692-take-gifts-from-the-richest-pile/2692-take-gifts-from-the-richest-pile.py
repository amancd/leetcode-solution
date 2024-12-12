class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for _ in range(k):
            max_value = max(gifts)
            idx = gifts.index(max_value)
            
            gifts[idx] = int(math.sqrt(max_value))
        
        return sum(gifts)
