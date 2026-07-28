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

        freq = {}
        for i in range(len(nums)):
            freq[nums[i]] = freq.get(nums[i],0)+1
        count = 0    
        for i in freq:
            if freq[i] > count:
                count = freq[i]
                n = i
        return n   
                      



        