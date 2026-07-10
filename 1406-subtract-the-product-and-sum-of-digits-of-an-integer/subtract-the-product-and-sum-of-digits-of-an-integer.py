class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        mul=1
        add=0
        for i in str(n):
            # i=int(i)
            mul=mul*int(i)
        # for j in str(n):
            add=add+int(i)
        return mul-add    
        
        # while n>0:
        #     dig=n%10
        #     mul=mul*dig
        #     add=add+dig
        #     n=n//10
        # return mul-add
             