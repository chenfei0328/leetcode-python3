class Solution:
    def countBits(self, num: int) -> List[int]:
        dp = [0] * (num + 1)
        pointer = 1
        i = 1
        while i < num + 1:
            for j in range(pointer):
                dp[i] = dp[j] + 1
                i += 1
                if i == num + 1:
                    break
            pointer *= 2
        
        return dp
