class Solution:
    def isHappy(self, n: int) -> bool:
        d = set()
        while True:
            num = 0
            while n > 0:
                num += (n % 10)**2
                n //= 10
            # print(num)
            if num == 1:
                return True
            else:
                if num in d:
                    return False
                else:
                    d.add(num)
                    n = num
                
        return False