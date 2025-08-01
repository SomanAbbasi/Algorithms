
class Stack:
    def __init__(self,size):
        self.size=size
        self.arr=[0]*size
        self.idx=-1
        
        
        
    #Push -> Append data in list. 
    def push(self,data):
        if self.idx>=self.size:
            print("Stack Overflow.")
            return False
        self.idx+=1
        self.arr[self.idx]=data
        return True

    #Pop -> Get Last data in list and then 
    
    def pop(self):
        if self.idx<0:
            
            print("Stack Underflow")
            return 0
        popped=self.arr[self.idx]
        self.idx-=1
        return popped
    
    #Peek/Top -> Get Just Top Data in list
    def peek(self):
        if self.idx<0:
            print("Stack is empty. ")
            return 0
        return self.arr[self.idx]
    
    #Is-Empty -> 
    def isEmpty(self):
        return self.idx<0


s1=Stack(5)

s1.push(10)
s1.push(40)
s1.push(30)

print(s1.pop()," Popped From a List.")

print("Top element is: ", s1.peek())

while not s1.isEmpty():
    print(s1.pop(), end=" ")
            
            
            