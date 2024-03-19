class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        n = len(nums)
        even_sum = sum(nums[i] for i in range(0, n, 2))
        odd_sum = sum(nums[i] for i in range(1, n, 2))
        count = 0
        
        prev_even_sum, prev_odd_sum = 0, 0
        
        for i in range(n):
            if i % 2 == 0:
                even_sum -= nums[i]
            else:
                odd_sum -= nums[i]
                
            if prev_even_sum + odd_sum == prev_odd_sum + even_sum:
                count += 1
                
            if i % 2 == 0:
                prev_even_sum += nums[i]
            else:
                prev_odd_sum += nums[i]
        
        return count