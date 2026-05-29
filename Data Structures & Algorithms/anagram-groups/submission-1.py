class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        ans = {}

        for s in strs:
            sign = "".join(sorted(s))
            if sign not in ans:
                ans[sign] = []
            ans[sign].append(s)
        return list(ans.values())