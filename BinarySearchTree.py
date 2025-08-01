class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def insert(self, data):
        if data == self.data:
            return
        if data < self.data:
            if self.left is None:
                self.left = BinarySearchTree(data)
            else:
                self.left.insert(data)
        else:
            if self.right is None:
                self.right = BinarySearchTree(data)
            else:
                self.right.insert(data)
                
    def delete(self, data):
        if data < self.data:
            if self.left:
                self.left = self.left.delete(data)
        elif data > self.data:
            if self.right:
                self.right = self.right.delete(data)
        else:
            # Node with only one child or no child
            if self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            
            # Node with two children: Get the inorder successor
            temp = self.right.find_min()
            self.data = temp.data
            self.right = self.right.delete(temp.data)
        
        return self
    
    def search(self, data):
        if data == self.data:
            return self
        elif data < self.data and self.left:
            return self.left.search(data)
        elif data > self.data and self.right:
            return self.right.search(data)
        else:
            return None
    
    def find_min(self):
        current = self
        while current.left:
            current = current.left
        return current
    
    def find_max(self):
        current = self
        while current.right:
            current = current.right
        return current
    
    def in_order_traversal(self):
        results = []
        if self.left:
            results += self.left.in_order_traversal()
        results.append(self.data)
        if self.right:
            results += self.right.in_order_traversal()
        return results
    
    def pre_order_traversal(self):
        results = [self.data]
        if self.left:
            results += self.left.pre_order_traversal()
        if self.right:
            results += self.right.pre_order_traversal()
        return results

    def post_order_traversal(self):
        results = []
        if self.left:
            results += self.left.post_order_traversal()
        if self.right:
            results += self.right.post_order_traversal()
        results.append(self.data)
        return results


root = BinarySearchTree(50)
root.insert(30)
root.insert(70)
root.insert(20)
root.insert(40)
root.insert(60)
root.insert(80)

print("Inorder:", root.in_order_traversal())     # [20, 30, 40, 50, 60, 70, 80]
print("Preorder:", root.pre_order_traversal())   # [50, 30, 20, 40, 70, 60, 80]
print("Postorder:", root.post_order_traversal()) # [20, 40, 30, 60, 80, 70, 50]
print("Search 40:", root.search(40))  # Should return node object
print("Min:", root.find_min().data)    # 20
print("Max:", root.find_max().data)    # 80


root = root.delete(30)
print("\nAfter deleting 30 (node with two children):")
print("Inorder:", root.in_order_traversal())