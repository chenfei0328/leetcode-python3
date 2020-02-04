class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1
        if right == -1:
            return [-1, -1]
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                break
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        i = j = mid
        if left > right:
            return [-1, -1]
        else:
            while i >= 0 and nums[i] == target:
                i -= 1
            while j <= len(nums) - 1 and nums[j] == target:
                j += 1
            return [i + 1, j - 1]