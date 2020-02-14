class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        left, right = 0, len(nums) - 1
        
        sorted_nums = sorted(nums)
        
        while left <= right and sorted_nums[left] == nums[left]:
            left += 1
        
        if left == right + 1:
            return 0
        
        while right >= 0 and sorted_nums[right] == nums[right]:
            right -= 1
            
        return right - left + 1