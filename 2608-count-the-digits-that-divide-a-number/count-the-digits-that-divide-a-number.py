class Solution:
    def countDigits(self, num: int) -> int:
        # count=0
        # org=num
        # while num!=0:
        #     d=num%10
        #     if org % d == 0:
        #         count+=1
        #     num//=10   
        # return count  

        return sum(num % int(d) == 0 for d in str(num))   






        