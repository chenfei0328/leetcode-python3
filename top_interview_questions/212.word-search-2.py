class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def dfs(i, j, node, path):
            if board[i][j] in node:
                board[i][j], letter = '', board[i][j]
                node, path = node[letter], path + letter
                if '*' in node: results.add(path)
                for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                    if 0 <= x < m and 0 <= y < n:
                        dfs(x, y, node, path)
                board[i][j] = letter

        tree, results, m, n = {}, set(), len(board), len(board) and len(board[0])

        for word in words:
            node = tree
            for letter in word + '*': node = node.setdefault(letter, {})
            print(node)
        [dfs(i, j, tree, '') for i in range(m) for j in range(n)]

        return list(results)

# Start with

# variable declarations

# trie = {}
# results = set()
# m = len(board)
# n = len(board) and len(board[0])

# loop through words
# assign node = trie
# loop through each letter of the word
# assign node to setdefault of letter {}
# add end of word marker

# loop through matrix coordinates calling dfs function passing coordinates, tree, and empty path
# (dfs(i, j, tree, ''))

# dfs function: dfs(i, j, node, path)
# check if these coordinates are in the trie/node
# clear out value from this location so it is not used by other neighbors
# do this by swapping it with another variable that you can use to put it back at the end
# assign the node to the value of the key (letter) and append the letter to the path
# if you find an end of word marker in this node then add the path (word) to the results set
# loop through adjacent neighbors
# call recursive function with eligible neighbors within grid boundaries
# assign the value back to the position

# return list of results


import copy
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board or not words:
            return []
            
        def dfs(i, j, index, word, b):
            letter = b[i][j]
            if letter != '':
                if word[index] == letter:
                    if index == len(word) - 1:
                        results.add(word)
                        return
                    else:
                        b[i][j] = ''
                        for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                            if 0 <= x < m and 0 <= y < n:
                                dfs(x, y, index + 1, word, b)
                        b[i][j] = letter
        
        m, n = len(board), len(board[0])
        results = set()
        for word in words:
            for i in range(m):
                for j in range(n):
                    b = copy.deepcopy(board)
                    dfs(i, j, 0, word, b)

        return results