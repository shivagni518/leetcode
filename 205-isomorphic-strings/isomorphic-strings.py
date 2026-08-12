class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        freq={}
        back={}
        for i in range(len(s)):
            if s[i] in freq:
                if freq[s[i]] != t[i]:
                    return False
            else:
                freq[s[i]] = t[i]
            if t[i] in back:
                if back[t[i]] != s[i]:
                    return False
            else:
                back[t[i]] = s[i]           
        return True     
        