class Solution:
    def isPalindrome(self, x: int) -> bool:
        # x1 = str(x)
        return str(x) == str(x)[::-1]
               
        