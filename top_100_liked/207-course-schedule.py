from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        d = defaultdict(list)
        for u, v in prerequisites:
            d[u].append(v)
        
        def dfs(u, visited=[]):
            if visited[u]:
                return True
            else:
                visited[u] = True
                for v in d[u]:
                    if dfs(v, visited):
                        return True
                    visited[v] = False
                return False
        
        for n in range(numCourses):
            l = [False for _ in range(numCourses)]
            if dfs(n, l):
                return False
        return True