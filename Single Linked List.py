class Node:
    def __init__(self,new_data):
        self.data=new_data
        self.next=None
    
    #Traversal of Single Linked List.
    
    def TraverseList(self):
        curr=self
        while curr is not None:
            print(curr.data,end=" ")
            curr=curr.next
    
    def searchkey(self,key):
        curr=self
        while curr is not None:
            if curr.data==key:
                return True
            curr=curr.next
            
        return False
    
    #Insert Node at the Start
    def insertion_at_front(self,new_data):
        
        #create a new node with the given data 
        new_data=Node(new_data)
        new_data.next=self
        
        return new_data
    #insetion at the end 
    def insertion_at_end(self,new_data):
        
        new_data=Node(new_data)
        if self is None:
            return new_data
        
        last=self
        while last.next:
            last=last.next
        
        last.next=new_data

        return self
            




head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
head.next.next.next=Node(40)

head.TraverseList()

print(head.searchkey(20))

print("Insertion at the front: ")
head=head.insertion_at_front(50)

head.TraverseList()

print("Insertion at the End: ")
head=head.insertion_at_end(500)

head.TraverseList()