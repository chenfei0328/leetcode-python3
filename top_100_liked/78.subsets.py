class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = [[]]
        
        for num in nums:
            ans += [item + [num] for item in ans]
        return ans




class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first=0, combination=[]):
            if len(combination) == k:
                ans.append(combination[:])
            for i in range(first, n):
                combination.append(nums[i])
                backtrack(i + 1, combination)
                combination.pop()
        
        ans = []
        n = len(nums)
        for k in range(n + 1):
            backtrack()
        return ans