class Solution:
    def countElements(self, arr: List[int]) -> int:
        
        num_set = set(arr)
        score = 0

        for num in arr:
            if num + 1 in num_set:
                score += 1
            
        return score