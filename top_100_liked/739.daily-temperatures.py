class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        ans = [0] * len(T)
        if len(T) < 2:
            return ans
        
        for i in range(len(T) - 2, -1, -1):
            if T[i] < T[i + 1]:
                ans[i] = 1
            else:
                k = i + 1
                while k <= len(T) - 1:
                    if T[k] > T[i]:
                        ans[i] = k - i
                        break
                    else:
                        if ans[k] == 0:
                            ans[i] = 0
                            break
                        else:
                            k += ans[k]          
                    
        return ans



class Solution(object):
    def dailyTemperatures(self, T):
        ans = [0] * len(T)
        stack = [] #indexes from hottest to coldest
        for i in range(len(T) - 1, -1, -1):
            while stack and T[i] >= T[stack[-1]]:
                stack.pop()
            if stack:
                ans[i] = stack[-1] - i
            stack.append(i)
        return ans