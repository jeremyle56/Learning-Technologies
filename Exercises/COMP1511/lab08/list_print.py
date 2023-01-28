class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def list_print(list):
    curr_node = list
    while curr_node:
        if curr_node.data == None:
            break
        print(str(curr_node.data) + ' -> ', end="")
        curr_node = curr_node.next
    print('X')

def array_to_list(length, input_arr):
    list = Node(None)
    i = length - 1
    while i >= 0:
        n = Node(input_arr[i])
        n.next = list
        list = n
        i = i - 1
    return list

def main():
    input_arr = list(map(int, input().split()))
    total_num = len(input_arr)
    
    head = array_to_list(total_num, input_arr)
    list_print(head)

main()