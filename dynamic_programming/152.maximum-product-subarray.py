class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        l = len(nums)
        res = pre_min = pre_max = nums[0]
        
        for i in range(1, l):
            tmp = pre_min
            pre_min = min(tmp * nums[i], pre_max * nums[i], nums[i])
            pre_max = max(tmp * nums[i], pre_max * nums[i], nums[i])
            
            if pre_max > res:
                res = pre_max
        
        return res
        

