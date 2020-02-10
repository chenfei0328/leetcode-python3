class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        low, fast = nums[0], nums[0]
        while True:
            low = nums[low]
            fast = nums[nums[fast]]
            if low == fast:
                break
        
        ptr1 = nums[0]
        ptr2 = low
        while ptr1 != ptr2:
            ptr1 = nums[ptr1]
            ptr2 = nums[ptr2]
        
        return ptr1