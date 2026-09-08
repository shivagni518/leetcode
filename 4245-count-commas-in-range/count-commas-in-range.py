class Solution:
    def countCommas(self, n: int) -> int:
        # s=str(n)
        # count = 0
        # for i in s:
        #     count+=1
        # if count <= 3:
        #     return 0 
        # elif count > 3 or count < 5:
        #     return 3



        count = 0
        for i in range(1, n + 1):
            count += f"{i:,}".count(",")

        return count      

        