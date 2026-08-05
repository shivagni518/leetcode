class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        num = sorted([i*i for i in nums]) 
        return num 

        # for i in range(len(nums)):
        #     nums[i] = nums[i]*nums[i]
        # nums.sort()
        # return nums 

        # ans=[]
        # for i in range(len(nums)):
        #     b=nums[i]*nums[i]
        #     ans.append(b)
        # ans.sort()
        # return ans     


            
            

           

        