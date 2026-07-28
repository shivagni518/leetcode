class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # max_num = 0
        # n=nums[0]
        # for i in range(len(nums)):
        #     count = 0
        #     for j in range(i,len(nums)):
        #         if nums[i] == nums[j]:
        #                 count += 1
        #     if count > max_num:
        #         max_num = count 
        #         n = nums[i]
        # return n    

        f = {}
        for i in nums:
            f[i] = f.get(i,0)+1
        count = 0    
        for i in f:
            if f[i] > count:
                count = f[i]
                n = i
        return n   
                      



        