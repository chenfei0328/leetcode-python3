class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = len(nums)
        if l < 2:
            return l
        
        k = 1
        for i in range(1, l):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1

        return k