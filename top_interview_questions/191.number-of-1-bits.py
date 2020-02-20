class Solution:
    def hammingWeight(self, n: int) -> int:
        b = bin(n)
        count = 0
        for i in range(len(b)):
            if b[i] == '1':
                count += 1
                
        return count
    
    
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n != 0:
            count += 1
            n &= (n - 1)
            
        return count