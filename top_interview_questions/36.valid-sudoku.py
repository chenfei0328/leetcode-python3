import collections
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        table = []
        for i in range(27):
            t = collections.defaultdict(int)
            table.append(t)
        
        for i in range(9):
            for j in range(9):
                x = board[i][j]
                if x != '.':
                    table[i][x] += 1
                    table[9 + j][x] += 1
                    box = i // 3 + j // 3 * 3 + 18
                    # print(box)
                    table[box][x] += 1
                    if table[i][x] > 1 or table[9 + j][x] > 1 or table[box][x] > 1:
                        return False
        # print(table[18])       
        return True