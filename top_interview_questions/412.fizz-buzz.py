class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        for i in range(1, n + 1):
            tmp = str(i)
            if i % 15 == 0:
                tmp = 'FizzBuzz'
            elif i % 3 == 0:
                tmp = 'Fizz'
            elif i % 5 == 0:
                tmp = 'Buzz'
                
            ans.append(tmp)
            
        return ans