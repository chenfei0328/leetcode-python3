import collections

class LRUCache:

    def __init__(self, capacity: int):
        self._dict = collections.OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self._dict:
            self._dict.move_to_end(key)
            return self._dict[key]
        return -1

    def put(self, key: int, value: int) -> None:
        self._dict[key] = value
        self._dict.move_to_end(key)
        
        if len(self._dict) > self.capacity:
            self._dict.popitem(last=False)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)