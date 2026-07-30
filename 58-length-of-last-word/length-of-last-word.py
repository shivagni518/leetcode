class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        w=s.split()
        # count=0
        # for i in range(len(w)-1,-1,-1):
        #     if w[i] != " ":
        #         count+=1
        #     else:         
        #         return count   

        return len(w[len(w)-1])


            

        