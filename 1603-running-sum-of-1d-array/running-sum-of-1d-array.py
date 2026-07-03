class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        S=[]
        sum=0
        for i in range(len(nums)):
            sum=sum+nums[i]
            S.append(sum)
        return S
