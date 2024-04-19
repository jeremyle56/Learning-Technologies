class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def array_to_list(length, input_arr):
    list = Node(input_arr[length - 1])
    i = length - 2
    while i >= 0:
        n = Node(input_arr[i])
        n.next = list
        list = n
        i = i - 1
    return list

def insert_tail(list, value):
    curr_node = list
    n = Node(value)
    while curr_node.next:
        curr_node = curr_node.next
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
    input_arr = list(map(int, input().split()))
    new_val = int(input("Enter number to insert to tail: "))
    
    head = array_to_list(num_nums, input_arr)
    head = insert_tail(head, new_val)
    print_list(head)

main()