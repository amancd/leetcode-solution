class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        
        num1 = []
        num2 = []

        for i in range(1, n+1):
            if i%m!=0:
                num1.append(i)
        
        print(num1)

        for i in range(1, n+1):
            if i%m==0:
                num2.append(i)
        
        print(num2)

        return (sum(num1) - sum(num2))