class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        l=[]
        for i in nums:
            count=0
            for j in nums:
                if j<i:
                    count+=1
            l.append(count)
        return l