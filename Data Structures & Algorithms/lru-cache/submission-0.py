class Node:
    def __init__(self,key=0,value=0):
        self.key = key
        self.val = value
        self.prev = None # double LL
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap=capacity
        self.cache={} # hashmap

        self.left=Node()
        self.right=Node()
        self.left.next=self.right
        self.right.prev=self.left

    def remove(self,node):
        nxt=node.next
        prev=node.prev
        nxt.prev=prev
        prev.next=nxt

    def add(self,node):
        prev=self.right.prev
        prev.next=node
        node.prev=prev
        self.right.prev=node
        node.next=self.right

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node=self.cache[key]
        self.remove(node)
        self.add(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])    # drop the old node from the list
        node=Node(key,value)
        self.cache[key]=node
        self.add(node)

        if len(self.cache)>self.cap:
            lru=self.left.next
            self.remove(lru)
            del self.cache[lru.key]

        
