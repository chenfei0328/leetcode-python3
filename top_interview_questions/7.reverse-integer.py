class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        
        if x > 0:
            result = int(str(x)[::-1])
        else:
            result = -int(str(x)[-1:0:-1])
        
        return result if result >= -2**31 and result <= 2**31 - 1 else 0
            