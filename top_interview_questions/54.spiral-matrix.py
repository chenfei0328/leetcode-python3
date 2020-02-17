class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return matrix
        
        i, j = 0, 0
        m, n = len(matrix) - 1, len(matrix[0]) - 1
        output = []
        while i <= m and j <= n:
            for k in range(j, n + 1):
                output.append(matrix[i][k])

            if i == m:
                return output

            for k in range(i + 1, m + 1):
                output.append(matrix[k][n])

            if j == n:
                return output

            for k in range(n - 1, j - 1, -1):
                output.append(matrix[m][k])
            for k in range(m - 1, i, -1):
                output.append(matrix[k][j])
                
            i += 1
            j += 1
            m -= 1
            n -= 1
        
        return output