class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1=set(nums1)
        n2=set(nums2)
        r = n1 & n2
        l = list(r)
        return l

        
        