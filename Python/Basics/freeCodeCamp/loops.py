
i = 1
while i <= 10:
    print(i)
    i += 1

print("Done with loop")

for letter in "Giraffe Academy":
    print(letter)

friends = ["Jim", "Karen", "Kevin"]
for name in friends:
    print(name)

for index in range(len(friends)):
    print(friends[index])

for index in range(3, 10):
    print(index)

for index in range(5):
    if index == 0:
        print("first Iteration")
    else:
        print("Not first")

def expotent(base_num, pow_num):
    result = 1
    for i in range(pow_num):
        result *= base_num
    
    return result

print(expotent(2, 3))