class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) < 3:
            return max(nums)
        
        pre_max, cur_max = 0, 0
        for now in nums:
            tmp = cur_max
            cur_max = max(pre_max + now, cur_max)
            pre_max = tmp
            
        return cur_max
