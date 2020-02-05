class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        i = j = -1
        k = 0
        while k < l:
            if nums[k] == 0:
                i += 1
                j += 1
                if k > 0:
                    nums[k] = nums[k - 1]
                if j > 0:
                    nums[j] = nums[j - 1]
                nums[i] = 0
            elif nums[k] == 1:
                j += 1
                if k > 0:
                    nums[k] = nums[k - 1]
                if j >= 0:
                    nums[j] = 1
            else:
                pass
            k += 1