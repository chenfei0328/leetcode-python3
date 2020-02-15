class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        l = len(nums)
        count = 0
        agg_sum = [0] * (l + 1)
        
        for i in range(l):
            agg_sum[i + 1] = agg_sum[i] + nums[i]
        
        for i in range(l):
            for j in range(i + 1, l + 1):
                if agg_sum[j] - agg_sum[i] == k:
                    count += 1
                    
        return count

    
    
    
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        l = len(nums)
        count = 0
        
        for i in range(l):
            agg_sum = 0
            for j in range(i, l):
                agg_sum += nums[j]
                if agg_sum == k:
                    count += 1
                    
        return count
    
    
    
    
import collections
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        agg_sum = 0
        t = collections.defaultdict(int)
        t[0] = 1
        
        for num in nums:
            agg_sum += num
            count += t[agg_sum - k]
            t[agg_sum] += 1
            # print(t)
                
        return count