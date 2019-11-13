class NumArray:
    def __init__(self, nums: List[int]):
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        self.array = nums

    def sumRange(self, i: int, j: int) -> int:
        #print(self.array)
        if i == 0:
            return self.array[j]
        else:
            return self.array[j] - self.array[i - 1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
