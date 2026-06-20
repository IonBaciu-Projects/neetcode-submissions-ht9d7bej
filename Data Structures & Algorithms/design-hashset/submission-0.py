class MyHashSet:

    def __init__(self):
        self.hashset = [[] for _ in range(1000)]

    def add(self, key: int) -> None:
        box = key % 1000
        if key not in self.hashset[box]:
            self.hashset[box].append(key)

    def remove(self, key: int) -> None:
        box = key % 1000
        if key in self.hashset[box]:
            self.hashset[box].remove(key)

    def contains(self, key: int) -> bool:
        box = key % 1000
        if key in self.hashset[box]:
            return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)