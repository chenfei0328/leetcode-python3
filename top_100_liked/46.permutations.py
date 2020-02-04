class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:       
        def backtrack(combination):
            if len(combination) == len(nums):
                ans.append(combination[:])
                return
            for num in nums:
                if num not in combination:
                    combination.append(num)
                    backtrack(combination)
                    combination.remove(num)
        
        ans = []
        combination = []
        backtrack(combination)
        return ans