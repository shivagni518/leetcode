class Solution:
    def isPalindrome(self, x: int) -> bool:
        # return str(x) == str(x)[::-1]

        x1 = str(x)
        y = x1[::-1]
        if y == x1:
            return True
        return False    
        
               
        