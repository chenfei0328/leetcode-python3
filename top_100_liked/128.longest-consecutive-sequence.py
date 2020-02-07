class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        table = {nums[0]: 1}
        maxConsecutive = 1
        for i in range(len(nums)):
            mid = nums[i]
            if mid in table:
                continue

            left = mid - 1
            right = mid + 1
            
            left_num, right_num = 0, 0
            if left in table:
                left_num = table[left]
            if right in table:
                right_num = table[right]
            
            table[mid] = 1 + left_num + right_num
            while left in table:
                # table[left] = table[mid]
                left -= 1
            table[left + 1] = table[mid]
            while right in table:
                # table[right] = table[mid]
                right += 1
            table[right - 1] = table[mid]
            
            maxConsecutive = max(maxConsecutive, table[mid])
        
        return maxConsecutive
    
    
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        num_set = set(nums)
        
        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_length = 1
                
                while current_num + 1 in num_set:
                    current_num += 1
                    current_length += 1
                
                longest = max(longest, current_length)
        
        return longest
    
    