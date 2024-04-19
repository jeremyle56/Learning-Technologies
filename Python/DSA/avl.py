class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insert(self.root, data)

    def _insert(self, node, data):
        if not node:
            return Node(data)
        elif data < node.data:
            node.left = self._insert(node.left, data)
        else:
            node.right = self._insert(node.right, data)

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        balance = self.get_balance(node)
        if balance > 1 and data < node.left.data:
            return self.right_rotate(node)
        if balance < -1 and data > node.right.data:
            return self.left_rotate(node)
        if balance > 1 and data > node.left.data:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)
        if balance < -1 and data < node.right.data:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def right_rotate(self, node):
        left_child = node.left
        right_grandchild = left_child.right
        left_child.right = node
        node.left = right_grandchild
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        left_child.height = 1 + max(self.get_height(left_child.left), self.get_height(left_child.right))
        return left_child

    def left_rotate(self, node):
        right_child = node.right
        left_grandchild = right_child.left
        right_child.left = node
        node.right = left_grandchild
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        right_child.height = 1 + max(self.get_height(right_child.left), self.get_height(right_child.right))
        return right_child

#Creating an instance of the AVLTree class
avltree = AVLTree()

#Inserting elements into the tree
avltree.insert(10)
avltree.insert(20)
avltree.insert(30)
avltree.insert(40)
avltree.insert(50)

#Searching for an element in the tree
print(avltree.search(40)) # should return True
print(avltree.search(60)) # should return False