class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        ans = ""

        for i in range(min(len(w) for w in strs)):
            for word in strs:
                if word[i] != strs[0][i]:
                    return ans
            ans += strs[0][i]
        return ans