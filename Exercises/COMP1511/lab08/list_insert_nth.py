class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def array_to_list(length, input_arr):
    if length == 0:
        return None

    list = Node(input_arr[length - 1])
    i = length - 2
    while i >= 0:
        n = Node(input_arr[i])
        n.next = list
        list = n
        i = i - 1
    return list

def insert_nth(pos, list, value):
    n = Node(value)
    if pos == 0:
        n.next = list
        list = n
        return list

    curr_node = list
    i = 0
    while curr_node.next and i == pos:
        curr_node = curr_node.next
        i = i + 1
    if curr_node is None:
        return list
    n.next = curr_node.next
    curr_node.next = n
    return list

def print_list(list):
    print("[", end="")
    curr_node = list
    while curr_node:
        print(curr_node.data, end="")
        if curr_node.next != None:
            print(", ", end="")
        curr_node = curr_node.next
    print("]")

def main():
    num_nums = int(input("How many numbers in initial list?: "))
    if num_nums != 0:
        input_arr = list(map(int, input().split()))
    else:
        input_arr = []
    pos, new_val = map(int, input("Enter position and value to insert: ").split())
    
    head = array_to_list(num_nums, input_arr)
    head = insert_nth(pos, head, new_val)
    print_list(head)

main()