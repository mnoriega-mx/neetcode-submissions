class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.uses = []

    def get(self, key: int) -> int:
        if key in self.cache:
            self.uses.remove(key)
            self.uses.append(key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.uses.remove(key)
        else:
            if len(self.cache) == self.capacity:
                del self.cache[self.uses[0]]
                self.uses.remove(self.uses[0])
        self.cache[key] = value
        self.uses.append(key)


            


        
