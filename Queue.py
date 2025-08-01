class Queue:
    def __init__(self):
        self.values=[]
    
    def enqueue(self,value):
        self.values.append(value)
    
    def dequeue(self):
        if not self.values:
            print("Queue is empty")
            return None
        front=self.values[0]
        self.values=self.values[1:]
        return front

q=Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print(q.dequeue())    
print(q.values)

