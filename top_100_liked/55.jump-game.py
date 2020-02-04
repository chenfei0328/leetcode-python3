class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i, max_index = 0, nums[0]
        while i < len(nums) and i <= max_index:
            max_index = max(max_index, i + nums[i])
            i += 1
        return i == len(nums)