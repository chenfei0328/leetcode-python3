class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        if l < 2:
            return nums
        
        i, k = 0, 0
        while i < l:
            if nums[k] == 0:
                nums.append(0)
                nums.pop(k)
            else:
                k += 1
            i += 1




class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l = len(nums)
        if l < 2:
            return nums

        lastNonZero = 0
        for i, val in enumerate(nums):
            if val != 0:
                nums[lastNonZero] = nums[i]
                lastNonZero += 1
        
        for i in range(lastNonZero, l):
            nums[i] = 0