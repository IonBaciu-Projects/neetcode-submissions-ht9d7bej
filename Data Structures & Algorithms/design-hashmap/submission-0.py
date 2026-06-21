class MyHashMap:

    def __init__(self):
        self.hashmap = [[] for _ in range(1000)]

    def put(self, key: int, value: int) -> None:
        box = key % 1000
        found = False
        for i, pair in enumerate(self.hashmap[box]):
            if pair[0] == key:
                self.hashmap[box][i] = (key, value)
                found = True
        
        if not found:
            self.hashmap[box].append((key, value))

    def get(self, key: int) -> int:
        box = key % 1000

        for pair in self.hashmap[box]:
            if pair[0] == key:
                return pair[1]
        
        return -1

    def remove(self, key: int) -> None:
        box = key % 1000

        for i, pair in enumerate(self.hashmap[box]):
            if pair[0] == key:
                self.hashmap[box].pop(i)

        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)