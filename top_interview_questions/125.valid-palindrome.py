class Solution:
    def isPalindrome(self, s: str) -> bool:
        char = ''
        for c in s:
            if c.isalpha():
                char += c.lower()
            elif c.isdigit():
                char += c
        
        return char == char[::-1]