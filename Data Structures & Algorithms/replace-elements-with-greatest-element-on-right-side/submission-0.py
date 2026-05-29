class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        n = len(arr)
        ans = [0] * n
        rightMax = -1

        for x in range(n -1, -1, -1):
            ans[x] = rightMax
            rightMax = max(rightMax, arr[x])
        
        return ans