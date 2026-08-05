"""
The key and value are both integers 
What if we used similar logic where we have a list 
with a million entries, but maybe not boolean logic this time. 

The key would be an index in the list.

The actual value would be put at that index. 
""" 
class MyHashMap:
    def __init__(self):
        self.ls = [-1] * (10**6 + 1)
    def put(self, key: int, value: int) -> None:
        self.ls[key] = value 
    def get(self, key: int) -> int:
        return self.ls[key] 
    def remove(self, key: int) -> None:
        self.ls[key] = -1 
# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)