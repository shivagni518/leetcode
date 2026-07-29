class Solution:
    def reverseWords(self, s: str) -> str:
        ans=""
        word=""
        for i in s:
            if i == " ":
                ans += word[::-1] + " "
                word = ""
            else:
                word += i 
        ans += word[::-1]  
        return ans         

        
        