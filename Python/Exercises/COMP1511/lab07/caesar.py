# More Elegant Solution

import re, sys


def caesar(n, line):
    line = re.sub(
        r"([a-z])",
        lambda c: chr(ord("a") + (ord(c.group(1)) - ord("a") + n) % 26),
        line,
    )
    line = re.sub(
        r"([A-Z])",
        lambda c: chr(ord("A") + (ord(c.group(1)) - ord("A") + n) % 26),
        line,
    )
    return line


def read_input():
    shift = int(input())

    for index, line in enumerate(sys.stdin):
        if index == 0:
            pass
        print(caesar(shift, line), end="")


read_input()

# First Attempt
# def caesar(shift, line):
#     result = []
#     for i in range(len(line)):
#         if line[i] >= 'a' and line[i] <= 'z':
#             result.append(chr(ord('a') + (ord(line[i]) - ord('a') + shift) % 26))
#         elif line[i] >= 'A' and line[i] <= 'Z':
#             result.append(chr(ord('A') + (ord(line[i]) - ord('A') + shift) % 26))
#         else: result.append(line[i])

#     return ''.join(result)

# def read_input():
#     shift = int(input())

#     while True:
#         try:
#             line = input()
#             print(caesar(shift, line))
#         except EOFError:
#             break

# read_input()
