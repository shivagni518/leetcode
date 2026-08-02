class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq1={}
        freq2={}
        for i in ransomNote:
            freq1[i] = freq1.get(i,0)+1
        for i in magazine:
            freq2[i] = freq2.get(i,0)+1

        for i in freq1:
            if freq1[i] > freq2.get(i,0):
                return False
        return True                  
        