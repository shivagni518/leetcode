class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        l=[]
        maxy=max(candies)
        for i in candies:
                if i+extraCandies>=maxy:
                    l.append(True)
                else:
                    l.append(False)       
        return l
        