class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        freq = {}

        def fn(num):
            t = 0
            while num!=0:
                t += num%10
                num = num//10
            
            return t

        for num in nums:
            t = fn(num)
            if t not in freq:
                freq[t] = [num]
            else:
                freq[t] += [num]
        
        print(freq)

        maximum = -1

        for k, v in freq.items():
            if len(v) >= 2:
                v.sort(reverse = True)
                maximum = max(maximum, v[0] + v[1])
            
        return maximum