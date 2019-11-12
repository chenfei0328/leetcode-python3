class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        
        # for i in range(1, n):
        #     for j in range(i + 1):
        #         if j == 0:
        #             triangle[i][j] += triangle[i - 1][j]
        #         elif j == i:
        #             triangle[i][j] += triangle[i - 1][j - 1]
        #         else:
        #             triangle[i][j] += min(triangle[i - 1][j], triangle[i - 1][j - 1])
        # return min(triangle[-1])
        
        for i in range(n - 2, -1, -1):
            for j in range(i + 1):
                triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1])
        return triangle[0][0]
