class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        ans = {}

        for i, x in enumerate(nums2):
            ans.setdefault(x, []).append(i)

        res = [ans[num].pop() for num in nums1]

        return res