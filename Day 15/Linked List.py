class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self,head,data): 
    #Complete this method
        new_node = Node(data)
        
        # If the list is empty, the new node becomes the head
        if head is None:
            return new_node
        
        # Traverse to the last node
        current = head
        while current.next:
            current = current.next
        
        # Set the last node's next to the new node
        current.next = new_node
        return head

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
mylist.display(head); 

