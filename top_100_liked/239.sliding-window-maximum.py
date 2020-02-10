class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return nums
        ans = []
        low, fast = 0, k
        ans.append(max(nums[:k]))
        
        while fast <= len(nums) - 1:
            if nums[fast] >= ans[-1]:
                ans.append(nums[fast])
            elif nums[low] == ans[-1]:
                ans.append(max(nums[low+1:fast+1]))
            else:
                ans.append(ans[-1])
            low, fast = low + 1, fast + 1
        
        return ans