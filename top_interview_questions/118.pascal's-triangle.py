class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]
        else:
            result = [[1], [1, 1]]
            for i in range(2, numRows):
                last = result[i - 1]
                tmp = [1]
                for j in range(0, len(last) - 1):
                    tmp.append(last[j] + last[j + 1])
                tmp.append(1)
                result.append(tmp)
                
            return result