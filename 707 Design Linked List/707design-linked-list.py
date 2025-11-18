# class MyLinkedList:

#     def __init__(self):
#         self.head=None

#     def get(self, index: int) -> int:
       
#         cnt=self.head
#         i=0
#         while cnt and i<index:
#             cnt=cnt.next
#             i+=1
#         return cnt.val if cnt and i==index else -1       
        

#     def addAtHead(self, val: int) -> None:
#         new=ListNode(val)
#         new.next=self.head
#         self.head=new
        

#     def addAtTail(self, val: int) -> None:
#         new=ListNode(val) 
#         if not self.head:
#             self.addAtHead(val)
#             return
#         cnt=self.head
#         while cnt.next:
#             cnt=cnt.next
           
#         cnt.next=new    
        

#     def addAtIndex(self, index: int, val: int) -> None:
#         if index==0:
#             self.addAtHead(val)
#             return
#         cnt=self.head
#         i=0
#         while cnt and i<index-1:
#             cnt=cnt.next
#             i+=1
#         if not cnt:
#             return    
#         new=ListNode(val)
#         new.next=cnt.next
#         cnt.next=new   
        

#     def deleteAtIndex(self, index: int) -> None:
#         if not self.head:
#             return
#         if index==0:
#             self.head=self.head.next  
#             return  

#         cnt=self.head
#         i=0
#         while cnt and i<index-1 :
#             cnt=cnt.next
#             i+=1
#         if not cnt or not cnt.next:
#             return 
#         cnt.next=cnt.next.next  


# class MyLinkedList:
#     def __init__(self):
#         self.dummy=ListNode()
#         self.size=0
#     def get(self,index:int) -> int: 
#         if index<0 or index>=self.size:
#             return -1
#         cnt=self.dummy.next
#         for i in range(index):
#             cnt=cnt.next
#         return cnt.val    

#     def addAtHead(self,val:int)-> None:
#         self.addAtIndex(0,val)

#     def addAtTail(self, val:int) ->None:
#         self.addAtIndex(self.size,val)

#     def addAtIndex(self,index:int,val:int) -> None:
#         if index<0 or index>self.size:
#             return 
#         perv=self.dummy
#         new=ListNode(val)
#         for _ in range(index):
#             perv=perv.next
#         new.next=perv.next    
#         perv.next=new
       
#         self.size+=1    


#     def deleteAtIndex(self,index:int) -> None: 
#       if index<0 or index>=self.size:
#         return
#       perv=self.dummy  
#       for _ in range(index):
#          perv=perv.next
#       perv.next=perv.next.next 
#       self.size-=1                  


class ListNode:
    def __init__(self,val):
        self.val=val
        self.prev=None
        self.next=None
class MyLinkedList:
    def __init__(self):
        self.right=ListNode(0)
        self.left=ListNode(0)
        self.left.next=self.right
        self.right.prev=self.left
    def get(self,index:int) ->int:
        cnt=self.left.next
        while cnt and index>0:
            cnt=cnt.next
            index-=1
        if cnt and cnt!=self.right and index==0:
            return cnt.val
        return -1        

    def addAtHead(self,val:int)->None:
     node,next,prev=ListNode(val),self.left.next,self.left
     prev.next=node
     next.prev=node
     node.next=next
     node.prev=prev


    def addAtTail(self,val:int)->None:
        node,next,prev=ListNode(val),self.right,self.right.prev
        prev.next=node
        next.prev=node
        node.next=next
        node.prev=prev

    def addAtIndex(self,index:int,val:int)->None:    
        if index<0:
            return
        cnt=self.left.next
        while cnt and index>0:
            cnt=cnt.next
            index-=1
        if cnt and index==0:
            node,next,prev=ListNode(val),cnt,cnt.prev
            prev.next=node
            next.prev=node
            node.next=next
            node.prev=prev

    def deleteAtIndex(self,index:int)->None:
       if index<0:
         return 
       cnt=self.left.next
       while cnt and index>0:
        cnt=cnt.next
        index-=1
       if cnt and cnt !=self.right and index==0:
           next, prev =cnt.next,cnt.prev
           prev.next=next
           next.prev=prev 


        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)