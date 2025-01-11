class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        
        if len(s) < k:
            return False

        counts = Counter(s)

        print(counts)

        count = 0
        for key, v in counts.items():
            if v%2!=0:
                count+=1

        if count <= k:
            return True

        return False