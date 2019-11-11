class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l = len(nums)
        dp = nums
        for i in range(1, l):
            dp[i] = max(nums[i], nums[i] + dp[i - 1])
        
        return max(dp)
