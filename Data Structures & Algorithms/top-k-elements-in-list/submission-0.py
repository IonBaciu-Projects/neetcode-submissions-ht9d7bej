class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hashMap = {}
        ans = []
        res = []
        i = 0

        for n in nums:
            hashMap[n] = hashMap.get(n, 0) + 1
        for m in range(len(nums) + 1):
            ans.append([])
        for num, freq in hashMap.items():
            ans[freq].append(num)
        for i in range(len(ans) -1, 0 , -1):
            for n in ans[i]:
                res.append(n)
                if len(res) == k:
                    return res
