class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))
        # print(people)
        
        ans = []
        for p in people:
            ans.insert(p[1], p)            
                        
        return ans
    
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))
        
        for i in range(len(people)):
            if people[i][1] != i:
                p = people.pop(i)
                people.insert(p[1], p)
            
        return people