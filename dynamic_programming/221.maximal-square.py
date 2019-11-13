class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        area = 0
        for i in range(0, m):
            for j in range(0, n):
                matrix[i][j] = int(matrix[i][j])
                if i == 0 or j == 0:
                    if area == 0:
                        area = max(area, matrix[i][j])
                else:
                    if matrix[i][j] == 1:
                        matrix[i][j] = 1 + min(matrix[i - 1][j - 1], matrix[i][j - 1], matrix[i - 1][j])
                        area = max(area, pow(matrix[i][j], 2))
        #print(matrix)
        return area
