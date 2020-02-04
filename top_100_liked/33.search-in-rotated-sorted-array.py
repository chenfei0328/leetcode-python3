class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums) - 1
        if j == -1:
            return -1
        if target >= nums[i]:
            while i < len(nums) and target >= nums[i]:
                if target == nums[i]:
                    return i
                i += 1
            return -1
        elif target <= nums[j]:
            while j >= 0 and target <= nums[j]:
                if target == nums[j]:
                    return j
                j -= 1
            return -1
        else:
            return -1