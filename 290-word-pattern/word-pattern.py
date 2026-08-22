class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        a=s.split()
        freq={}
        back={}
        if len(pattern) != len(a):
            return False
        for i in range(len(pattern)):
            if pattern[i] in freq:
                if freq[pattern[i]] != a[i]:
                    return False
            else:
                freq[pattern[i]] = a[i]
            if a[i] in back:
                if back[a[i]] != pattern[i]:
                    return False
            else:
                back[a[i]] = pattern[i]            
        return True                 
        