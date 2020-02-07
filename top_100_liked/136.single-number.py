class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        table = {}
        for num in nums:
            if num in table:
                table.pop(num)
            else:
                table[num] = 1
        return table.popitem()[0]
    
    
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return 2 * sum(set(nums)) - sum(nums)
   

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = 0
        for num in nums:
            a = a^num
        return a