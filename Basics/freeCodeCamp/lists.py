
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]

print(friends)
print(friends[1])
print(friends[-1])
print(friends[1:])
print(friends[1:3])
friends[1] = "Mike"
print(friends[1])

lucky_numbers = [4, 8, 15, 16, 23, 42, 69]
random_numbers = [1, 2, 3, 4]
lucky_numbers.extend(random_numbers)
random_numbers.append(7)
random_numbers.insert(1, 43)
lucky_numbers.remove(69)
print(lucky_numbers)
print(random_numbers)
random_numbers.clear()
lucky_numbers.pop()
print(random_numbers)
print(lucky_numbers)
print(lucky_numbers.index(16))
lucky_numbers.insert(5, 23)
print(lucky_numbers.count(23))
lucky_numbers.sort()
lucky_numbers.reverse()
print(lucky_numbers)

friends2 = friends.copy()
print(friends2)