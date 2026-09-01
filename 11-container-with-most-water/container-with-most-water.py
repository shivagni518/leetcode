class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height)-1
        maxWater = 0
        while start < end:
            b = end - start
            h = min(height[start],height[end])
            maxWater = max(maxWater,h*b)
            if height[start] < height[end]:
                start +=1
            else:
                end -=1    
        return maxWater 





        