class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans = []

        for i in range(len(boxes)):
            count = 0
            for j in range(len(boxes)):
                if i!=j:
                    if boxes[j] != '0':
                        count += abs(i-j)
            
            ans.append(count)
        
        return ans
