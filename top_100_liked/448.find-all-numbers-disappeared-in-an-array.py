class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        result = list(range(1, n + 1))
        for num in nums:
            result[num-1] = 0
        for i in range(n - 1, -1, -1):
            if result[i] == 0:
                result.pop(i)
                
        return result