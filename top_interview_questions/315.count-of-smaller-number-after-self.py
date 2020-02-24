class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        arr = sorted(nums)
        ans = [None] * len(nums)
        for i in range(len(nums)):
            # print(arr)
            # print(ans)
            j = arr.index(nums[i])
            ans[i] = j
            arr.pop(j)
        return ans