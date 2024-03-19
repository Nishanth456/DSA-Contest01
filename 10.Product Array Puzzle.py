class Solution:
    def productExceptSelf(self, nums, n):
        left_products = [0] * n
        right_products = [0] * n
        
        left_product = 1
        right_product = 1
        
        for i in range(n):
            left_products[i] = left_product
            left_product *= nums[i]
        
        for i in range(n - 1, -1, -1):
            right_products[i] = right_product
            right_product *= nums[i]
        
        result = [0] * n
        for i in range(n):
            result[i] = left_products[i] * right_products[i]
        
        return result
