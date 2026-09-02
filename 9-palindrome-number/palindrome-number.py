class Solution:
    def isPalindrome(self, x: int) -> bool:
        x1 = str(x)
        y = x1[::-1]
        if x1 == y:
            return True
        return False    
        