class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    
    
    def remove(self,index):
        if not self.head:
            return
        temp=self.head
        if index==0:
            self.head=temp.next
            temp=None
            return
        
        for i in range(index-1):
            temp=temp.next
            if not temp:
                return
        if not temp.next:
            return
        next_node=temp.next.next
        temp.next=None
        temp.next=next_node
 
    
    def print(self):
        current = self.head
        while current:
            print(current.data, end=" --> ")
            current = current.next
        print("None")
    
    
    def reverse(self):
        stack=[]
        current=self.head
        while current:
            stack.append(current)
            current=current.next
        if stack:
            self.head=stack.pop()
            current=self.head
            while stack:
                current.next=stack.pop()
                current=current.next
            current.next=None
    # def reverse(self):
    #     prev = None
    #     current = self.head
    #     while current:
    #         next_node = current.next
    #         current.next = prev
    #         prev = current
    #         current = next_node
    #     self.head = prev
    
    def merge_sorted(self, llist):
        p = self.head
        q = llist.head
        dummy_node = Node(0)
        current = dummy_node

        while p and q:
            if p.data < q.data:
                current.next = p
                p = p.next
            else:
                current.next = q
                q = q.next
            current = current.next
        
        if p:
            current.next = p
        if q:
            current.next = q
        
        self.head = dummy_node.next


ll1 = LinkedList()
ll1.insert_end(10)
ll1.insert_end(20)
ll1.insert_end(30)
ll1.insert_end(40)

print("Original Linked List 1:")
ll1.print()


ll2 = LinkedList()
ll2.insert_end(5)
ll2.insert_end(15)
ll2.insert_end(25)
ll2.insert_end(35)

print("Original Linked List 2:")
ll2.print()


ll1.merge_sorted(ll2)
print("Merged Sorted Linked List:")
ll1.print()


ll1.reverse()
print("Reversed Merged Linked List:")
ll1.print()


ll1.remove(3)
print("Linked List after removing node at index 3:")
ll1.print()
