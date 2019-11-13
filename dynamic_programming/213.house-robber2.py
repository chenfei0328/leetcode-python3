class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) < 4:
            return max(nums)
        return max(self.find(nums[1:]), self.find(nums[:-1]))
        
    def find(self, nums):
        pre_max, cur_max = 0, 0
        for now in nums:
            tmp = cur_max
            cur_max = max(pre_max + now, cur_max)
            pre_max = tmp
            
        return cur_max
