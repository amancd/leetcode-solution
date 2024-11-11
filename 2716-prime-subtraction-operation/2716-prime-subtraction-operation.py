class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        def is_prime(num):
            if num < 2:
                return False
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    return False
            return True

        def check_prime(n):
            primes = []
            for i in range(n - 1, 1, -1):
                if is_prime(i):
                    primes.append(i)
            return primes

        if nums == sorted(nums) and len(set(nums)) == len(nums):
            return True

        for i in range(len(nums)):
            temp = check_prime(nums[i])
            for n in temp:
                if i == 0 or (nums[i] - n) > nums[i - 1]:
                    nums[i] = nums[i] - n
                    break

        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                return False
        return True
