class Solution: 
    def countPrimes(self, n):
        if n < 3: return 0
        count = 0
        isPrime = [True] * (n + 1)
        isPrime[0] = False
        isPrime[1] = False
        for i in range(2, n):
            if isPrime[i]:
                count += 1
                for j in range(i * i, n, i):
                    isPrime[j] = False
        return count