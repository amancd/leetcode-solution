class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_products = [1] * n
        right_products = [1] * n

        left = 1
        for i in range(1, n):
            left *= nums[i-1]
            left_products[i] = left
        
        right=1
        for i in range(n-2, -1, -1):
            right *= nums[i+1]
            right_products[i] = right
        
        result = []
        for i in range(n):
            result.append(left_products[i] * right_products[i])
        
        return result