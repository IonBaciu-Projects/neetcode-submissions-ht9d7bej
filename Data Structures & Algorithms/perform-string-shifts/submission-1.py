class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        
        for d, a in shift:
            a %= len(s)
            if d == 0:
                s = s[a:] + s[:a]
            else:
                s = s[-a:] + s[:-a]
        return s