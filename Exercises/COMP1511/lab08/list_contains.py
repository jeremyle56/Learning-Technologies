class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def check_word(word, list):
    curr_node = list
    while curr_node:
        if curr_node.data == word:
            return 1;
        curr_node = curr_node.next

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
    num_strings = int(input("How many strings in initial list?: "))
    strings = []
    for i in range(num_strings):
        strings.append(input())
    
    head = array_to_list(num_strings, strings)

    word = input("Enter word to check contained: ")
    print(check_word(word, head))

main()