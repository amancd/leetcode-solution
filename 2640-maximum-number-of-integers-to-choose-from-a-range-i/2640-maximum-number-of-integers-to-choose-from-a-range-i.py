class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
            
        ban = set()

        for i in range(len(banned)):
            if banned[i]<=n and banned[i]>=1:
                ban.add(banned[i])

        total = 0
        count = 0
        for i in range(1, n+1):
            if i not in ban:
                total+= i
                count+= 1
                if total>maxSum:
                    total-=i
                    count-=1
                if total==maxSum:
                    return count

        return count