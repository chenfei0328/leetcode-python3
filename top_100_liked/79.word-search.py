class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:        
        def backtrack(i, j, index=0, check=[]):
            nonlocal flag
            if flag:
                return
            
            if board[i][j] == word[index]:
                check.append([i, j])
                index += 1
                if index == len(word):
                    flag = True
                    return
                
                if i - 1 >= 0 and [i - 1, j] not in check:
                    backtrack(i - 1, j, index)
                if i + 1 <= m - 1 and [i + 1, j] not in check:
                    backtrack(i + 1, j, index)
                if j - 1 >= 0 and [i, j - 1] not in check:
                    backtrack(i, j - 1, index)
                if j + 1 <= n - 1 and [i, j + 1] not in check:
                    backtrack(i, j + 1, index)
                
                check.pop()
        
        flag = False
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                backtrack(i, j)
                if flag:
                    return flag
        return flag