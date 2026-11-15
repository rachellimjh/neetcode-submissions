class Node:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.prev=None
        self.next=None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap=capacity
        self.store={} # key:node
        self.left=Node(0,0)
        self.right=Node(0,0)

        self.left.next=self.right
        self.right.prev=self.left

    def remove(self,node):
        prev=node.prev
        nxt=node.next

        prev.next=nxt
        nxt.prev=prev

    def add(self,node):
        prev=self.right.prev
        prev.next=node
        node.prev=prev
        self.right.prev=node
        node.next=self.right
    

    def get(self, key: int) -> int:
        if key in self.store:
            self.remove(self.store[key])
            self.add(self.store[key])
            return self.store[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.store:
            self.remove(self.store[key])

        node=Node(key,value) # rmb to create the node first
        self.add(node) 
        self.store[key]=node
        
        if self.cap<len(self.store):
            lru=self.left.next
            self.remove(lru)
            del self.store[lru.key]
