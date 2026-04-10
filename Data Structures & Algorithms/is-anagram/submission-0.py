class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        s_map = []
        t_map = []

        for char in s:
            s_map.append(char)
        for char in t:
            t_map.append(char)

        if sorted(s_map) == sorted(t_map):
            return True
        return False
