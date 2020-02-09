class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        major = nums[0]
        times = 1
        for i, num in enumerate(nums):
            if num not in d:
                if i < len(nums) / 2:
                    d[num] = 1
                else:
                    continue
            else:
                d[num] += 1
                if d[num] > times:
                    times = d[num]
                    major = num
            if times > len(nums) / 2:
                return major

            
import collections            
class Solution:
    def majorityElement(self, nums):
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)
    
class Solution:
    def majorityElement(self, nums):
        nums.sort()
        return nums[len(nums)//2]