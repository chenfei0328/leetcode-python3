class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums:
            return 1
        candidates = set()
        duplicates = set()
        
        def insert(num):
            if num in duplicates:
                if num in candidates:
                    candidates.remove(num)
            else:
                candidates.add(num)   
        
        for i in range(len(nums)):
            if nums[i] <= 0:
                insert(1) 
            elif nums[i] == 1:
                duplicates.add(1)
                if 1 in candidates:
                    candidates.remove(1)
                insert(2)
            else:
                duplicates.add(nums[i])
                if nums[i] in candidates:
                    candidates.remove(nums[i])
                insert(1)
                insert(nums[i] + 1)

        return min(candidates)