class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        def swap(x, y, a, b):
            matrix[x][y], matrix[a][b] = matrix[a][b], matrix[x][y]
        
        n = len(matrix)
        for i in range(n // 2 + 1):
            for j in range(i, n - i - 1):
                swap(i, j, j, n-i-1)
                swap(i, j, n-i-1, n-j-1)
                swap(i, j, n-j-1, i)
                