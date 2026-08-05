class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # num = sorted([i*i for i in nums]) 
        # return num 

        for i in range(len(nums)):
            nums[i] = nums[i]*nums[i]
        nums.sort()
        return nums  


            
            

           

        