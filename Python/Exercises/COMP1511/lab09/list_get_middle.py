import math

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def list_get_middle(size, list):
    if size == 1: 
        return list.data

    curr_node = list
    for i in range(math.ceil(size / 2 - 1)):
        curr_node = curr_node.next
    return curr_node.data

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
    num_nums = int(input("How many numbers in initial list?: "))
    if num_nums != 0:
        input_arr = list(map(int, input().split()))
    else:
        print(1)
        return
    
    head = array_to_list(num_nums, input_arr)
    print(list_get_middle(num_nums, head))

main()