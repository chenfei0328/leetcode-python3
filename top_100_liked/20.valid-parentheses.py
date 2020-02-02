class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                stack.append(s[i])
            elif s[i] == ')':
                if stack and stack[-1] == '(':
                    del stack[-1]
                else:
                    return False
            elif s[i] == '}':
                if stack and stack[-1] == '{':
                    del stack[-1]
                else:
                    return False
            elif s[i] == ']':
                if stack and stack[-1] == '[':
                    del stack[-1]
                else:
                    return False
        if len(stack) == 0:
            return True