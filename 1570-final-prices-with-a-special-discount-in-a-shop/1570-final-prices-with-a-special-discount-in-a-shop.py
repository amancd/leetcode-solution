class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        
        answer = []
        for i in range(len(prices)):
            res = False
            for j in range(i+1, len(prices)):
                if prices[i]>=prices[j]:
                    answer.append(prices[i] - prices[j])
                    res = True
                    break
            
            if res == False:
                answer.append(prices[i])

        return answer