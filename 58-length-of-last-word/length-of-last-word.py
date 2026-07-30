class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        w=s.split()
        # return len(w[len(w)-1])

        return len(w[-1])
            

        