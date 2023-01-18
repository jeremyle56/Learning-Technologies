class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
        
    def insert(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
        else:
            curr = self.root
            while True:
                if data < curr.data:
                    if curr.left is None:
                        curr.left = new_node
                        break
                    else:
                        curr = curr.left
                else:
                    if curr.right is None:
                        curr.right = new_node
                        break
                    else:
                        curr = curr.right
                        
    def search(self, key):
        curr = self.root
        while curr is not None:
            if curr.data == key:
                return True
            elif key < curr.data:
                curr = curr.left
            else:
                curr = curr.right
        return False

bst = BST()
bst.insert(50)
bst.insert(30)
bst.insert(20)
bst.insert(40)
bst.insert(70)
bst.insert(60)
bst.insert(80)

print(bst.search(20)) #True
print(bst.search(90)) #False