class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sign = {}
        for i in range(len(nums)):
            num = nums[i]
            if num in sign:
                return [sign[num], i]
            else:
                sign[target - num] = i