class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        return heapq.nsmallest(k, heapq.merge(*matrix))[-1]
    
    
    
import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        m, n = len(matrix), len(matrix[0])
        
        for j in range(n):
            heapq.heappush(heap, (matrix[0][j], 0, j))
            
        while k > 0:
            cur, row, col = heapq.heappop(heap)
            k -= 1
            if row + 1 < m:
                heapq.heappush(heap, (matrix[row + 1][col], row + 1, col))
                
        return cur