class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        l = len(digits)
        i = l - 1
        
        while i >= 0:
            num = digits[i]
            if num + 1 < 10:
                digits[i] = num + 1
                return digits
            else:
                digits[i] = 0
                if i == 0:
                    digits.insert(0, 1)
                    return digits
            i -= 1