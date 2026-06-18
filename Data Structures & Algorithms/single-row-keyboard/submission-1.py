class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        pos = {char : i for i, char in enumerate(keyboard)}

        prev = 0
        time = 0

        for char in word:
            curr = pos[char]
            time += abs(prev - curr)
            prev = pos[char]

        return time
            