class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:

        arr = [0] * 1001

        for num in nums:
            arr[num] += 1

        for num in range(1000, -1, -1):
            if arr[num] == 1:
                return num
                

        return -1
