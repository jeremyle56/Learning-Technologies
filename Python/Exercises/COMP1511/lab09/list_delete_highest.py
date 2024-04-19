class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def list_delete_value(list, value):
    if list == None:
        return None
    elif list.data == value:
        list = list.next
    
    curr = list
    prev = None

    while curr:
        while curr and curr.data != value:
            prev = curr
            curr = curr.next
        if not curr:
            return list
        prev.next = curr.next
        curr = prev.next
    return list


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
    num_nums = int(input("Total numbers in list: "))
    if num_nums != 0:
        input_arr = list(map(int, input().split()))
    else:
        print([])
        return
    
    value = max(input_arr)
    head = array_to_list(num_nums, input_arr)
    head = list_delete_value(head, value)
    print_list(head)

main()