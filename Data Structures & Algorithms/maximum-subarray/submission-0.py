class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        sum_so_far = 0
        for num in nums:
            sum_so_far = max(num, sum_so_far + num)
            max_sum = max(max_sum, sum_so_far)
        
        return max_sum