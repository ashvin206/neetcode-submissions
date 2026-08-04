"""
first call we add 1 
second call we add 2 
[1, 1, 0, ...] 
[1, 2] 
then we check if it contains 
"""
class MyHashSet:
    def __init__(self):
        self.ls = [False] * (10**6 + 1) 
    def add(self, key: int) -> None:
        self.ls[key] = True 
    def remove(self, key: int) -> None:
        if self.ls[key]:
            self.ls[key] = False 
    def contains(self, key: int) -> bool:
        if self.ls[key]:
            return True 
        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)