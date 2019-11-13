class Solution:
    def nthUglyNumber(self, n: int) -> int:
        res = [1]
        A, B, C = 2, 3, 5
        A_count = B_count = C_count = 0
        
        while len(res) < n:
            while A * res[A_count] <= res[-1]:
                A_count += 1
            while B * res[B_count] <= res[-1]:
                B_count += 1
            while C * res[C_count] <= res[-1]:
                C_count += 1
                
            res_next = min(A * res[A_count], B * res[B_count], C * res[C_count])
            res.append(res_next)
        
        return res[-1]
