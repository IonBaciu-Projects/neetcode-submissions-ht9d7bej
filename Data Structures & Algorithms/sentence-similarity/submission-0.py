class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        
        if len(sentence1) != len(sentence2):
            return False

        similar = set()

        for a, b in similarPairs:
            similar.add((a, b))
            similar.add((b, a))

        for x, y in zip(sentence1, sentence2):
            if x != y and (x,y) not in similar:
                return False
        
        return True