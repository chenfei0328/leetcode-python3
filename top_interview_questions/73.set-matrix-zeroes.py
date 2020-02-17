class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        m, n = len(matrix), len(matrix[0])
        col = set()
        
        for i in range(m):
            row = False
            for j in range(n):
                if matrix[i][j] == 0:
                    row = True
                    col.add(j)
            if row:
                for j in range(n):
                    matrix[i][j] = 0
                    
        for j in col:
            for i in range(m):
                matrix[i][j] = 0
                    