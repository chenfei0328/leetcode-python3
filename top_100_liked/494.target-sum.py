class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        l = len(nums)
        
        dp = [0] * 2001
        dp[nums[0] + 1000] = 1
        dp[-nums[0] + 1000] += 1
        
        for i in range(1, l):
            new = [0] * 2001
            for s in range(-1000, 1001):
                if dp[s + 1000] > 0:
                    new[s + nums[i] + 1000] += dp[s + 1000]
                    new[s - nums[i] + 1000] += dp[s + 1000]
            dp = new
        
        return 0 if S > 1000 or S < -1000 else dp[S + 1000]