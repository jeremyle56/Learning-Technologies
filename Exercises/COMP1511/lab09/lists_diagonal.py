class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class List_Node:
    def __init__(self):
        self.my_list = None
        self.next = None

def has_diagonal(head):
    has = 1
    i = 0
    num = head.my_list.data
    while head:
        j = 0
        n = head.my_list
        while n:
            if j == i and n.data != num:
                has = 0
            n = n.next
            j = j + 1
        i = i + 1
        head = head.next
    return has

def make_list(a, b, c):
    n = Node(a)
    n.next = Node(b)
    n.next.next = Node(c)
    return n

def main():
    head = List_Node()
    l = head
    l.my_list = make_list(5, 0, 0)

    l.next = List_Node()
    l = l.next
    l.my_list = make_list(0, 5, 0)

    l.next = List_Node()
    l = l.next
    l.my_list = make_list(0, 0, 5)

    print("The result of has_diagonal is: " + str(has_diagonal(head)))

main()