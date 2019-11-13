class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        l = len(nums)
        if l < 2:
            return l

        dp = [0] * l
        dp[0] = 1
        res = 1
        for i in range(1, l):
            j = i
            if nums[i] <= nums[i - 1]:
                while j >= 0:
                    if nums[i] > nums[j]:
                        dp[i] = dp[j] + 1
                        break
                    j -= 1
                if j == -1:
                    dp[i] = 1
            else:
                now = dp[i - 1] + 1
                while j >= 0:
                    if nums[i] > nums[j]:
                        now = max(now, dp[j] + 1)
                    j -= 1
                dp[i] = now
            res = max(res, dp[i])
        #print(dp)
        return res
        
                    
        
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        res = [1]
        for i in range(1, len(nums)):
            tmp = 1
            for j in range(i): # Check all numbers before i
                if nums[j] < nums[i]:
                    tmp = max(tmp, res[j] + 1)
            res.append(tmp)
        return max(res)



class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        res = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] > res[-1]:
                res.append(nums[i])
            else: # Call B search to find the most left number in res list, which is larger than the new number.
                left = 0
                right = len(res)-1
                while left < right:
                    mid = left + (right - left)//2
                    if res[mid] < nums[i]:
                        left = mid + 1
                    else: # need the most left number in res list, so right = mid, not right = mid - 1
                        right = mid                
                res[right] = nums[i]
            #print(res)
        return len(res)
