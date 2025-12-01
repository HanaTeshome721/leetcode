# class Node:
#     def __init__(self,key,value):
#         self.key=key
#         self.value=value
#         self.next=None
#         self.prev=None

# class LRUCache:

#     def __init__(self, capacity: int):
#         self.cap=capacity
#         self.cache={}
#         self.left=Node(0,0)
#         self.right=Node(0,0)
#         self.left.next=self.right
#         self.right.prev=self.left
        
#     def remove(self,node):
#         prev,next=node.prev,node.next
#         prev.next=next
#         next.prev=prev
#         node.next=None
#         node.prev=None
#     def insert(self,node):  
#         prev,next=self.right.prev ,self.right
#         prev.next=node
#         next.prev=node
#         node.next=next
#         node.prev=prev  
#     def get(self, key: int) -> int:
#         if key in self.cache:
#             self.remove(self.cache[key])
#             self.insert(self.cache[key])
#             return self.cache[key].value
#         return -1        
        

#     def put(self, key: int, value: int) -> None:
#         if key in self.cache:
#             self.remove(self.cache[key])
#         self.cache[key]=Node(key,value)
#         self.insert(self.cache[key])

#         if len(self.cache) > self.cap:
#             rm=self.left.next
#             self.remove(rm)
#             del self.cache[rm.key]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

class LRUCache:
    def __init__(self,capacity:int):
        self.cap=capacity
        self.cache=OrderedDict()
    def get(self,key:int)-> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]    

    def put(self,key:int,value:int)->None:
        if key in self.cache:
            self.cache[key]=value
            self.cache.move_to_end(key)
        else:
            self.cache[key]=value
            self.cache.move_to_end(key)
            if len(self.cache)>self.cap:
                self.cache.popitem(0)        

