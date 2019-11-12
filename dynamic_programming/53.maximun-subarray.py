class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l = len(nums)
        for i in range(1, l):
            nums[i] = max(nums[i], nums[i] + nums[i - 1])
        
        return max(nums)
