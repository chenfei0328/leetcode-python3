class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        ans = [1] * N
        
        right = 1
        for i in reversed(range(N)):
            ans[i] = right
            right *= nums[i]
            
        left = 1
        for i in range(N):
            ans[i] *= left
            left *= nums[i]
            
        return ans