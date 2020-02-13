class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if len(nums) < 2 or sum(nums) % 2 == 1:
            return False
        
        halfSum = sum(nums) // 2
        dp = [False] * (halfSum + 1)
        dp[0] = True
        for num in nums:
            for i in range(halfSum, num-1, -1):
                dp[i] = dp[i] or dp[i-num]
            # print(dp)
        
        return dp[halfSum]




class Solution:
    def canPartition(self, nums: List[int]) -> bool:
    	if len(nums) < 2 or sum(nums) % 2 == 1:
            return False
        
        # nums.sort()
        def backtrack(res, index):
            if index < 0:
                return False
            
            curr = nums[index]
            if curr == res:
                return True
            
            if curr < res:
                if backtrack(res-curr, index-1):
                    return True
            
            return backtrack(res, index-1)
        
        return backtrack(sum(nums) // 2, len(nums) - 1)