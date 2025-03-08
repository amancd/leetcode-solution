class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        
        left = 0
        right = 0
        
        minimum = float('inf')
        while right < len(blocks):
            if right - left < (k - 1) and right < len(blocks):
                right+=1
                continue
            
            if right - left > (k - 1):
                left+=1
                continue

            if right - left == (k - 1) and right < len(blocks):
                minimum = min(blocks[left:right+1].count('W'), minimum)
                left+=1
                right+=1
                continue
            
            left+=1
            right+=1
  
        
        return minimum