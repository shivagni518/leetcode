class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s1=""
        t1=""
        for ch in s:
            if ch != "#":
                s1 += ch
            else:
                # if s1:
                s1 = s1[:-1]
        for ch in t:
            if ch != "#":
                t1 += ch
            else:
                # if t1:
                t1 = t1[:-1]
        return s1 == t1
                         
        