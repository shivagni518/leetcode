class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        # rev1=int(str(num)[::-1])
        # rev2=int(str(rev1)[::-1])
        # return num==rev2

        if num%10!=0 or num==0:
            return True
        else:
            return False
        


            


        