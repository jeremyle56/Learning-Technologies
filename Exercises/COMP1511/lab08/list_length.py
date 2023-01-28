class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def length(list):
    curr_node = list
    i = 0
    while curr_node:
        curr_node = curr_node.next
        i = i + 1
    return i

def array_to_list(length, input_arr):
    list = Node(input_arr[length - 1])
    i = length - 2
    while i >= 0:
        n = Node(input_arr[i])
        n.next = list
        list = n
        i = i - 1
    return list

def main():
    num_nums = int(input("How many numbers in initial list?: "))
    input_arr = list(map(int, input().split()))
    
    head = array_to_list(num_nums, input_arr)
    print("Counted " + str(length(head)) + " elements in linked list.")

main()