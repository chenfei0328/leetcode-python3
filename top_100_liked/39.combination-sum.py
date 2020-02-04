import copy
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        
        def findTarget(res, index):
            if index < 0:
                return

            sumOfCombination = 0
            current = candidates[index]
            while sumOfCombination < res:
                combination.append(current)
                sumOfCombination += current
            
            if sumOfCombination == res:
                temp = copy.deepcopy(combination)
                ans.append(temp)
            
            while combination and combination[-1] == current:
                combination.pop()
                sumOfCombination -= current
                findTarget(res-sumOfCombination, index-1)
        
        ans = []
        combination = []
        findTarget(target, len(candidates) - 1)

        return ans