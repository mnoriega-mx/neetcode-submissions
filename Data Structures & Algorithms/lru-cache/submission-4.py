class Node:

    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # key to nodes
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.head.prev = self.head

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            #remove
            node.prev.next = node.next
            node.next.prev = node.prev
            #insert
            node.next = self.head.next
            node.prev = self.head
            self.head.next.prev = node
            self.head.next = node
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if len(self.cache) == self.capacity:
            if key not in self.cache:
                node = self.tail.prev
                #remove
                node.prev.next = node.next
                node.next.prev = node.prev
                del self.cache[node.key]
        
        if key in self.cache:
            node = self.cache[key]
            #remove
            node.prev.next = node.next
            node.next.prev = node.prev

        node = Node(key, value)
        self.cache[key] = node
        #insert
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        