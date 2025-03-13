def add_one(some_list):
    lst = int(''.join(map(str, some_list)))
    lst += 1
    lst2 = [int(some_list) for some_list in str(lst)]
    return lst2
print(add_one([9]))

assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5]
assert add_one([9, 9, 9]) == [1, 0, 0, 0]
assert add_one([0]) == [1]
assert add_one([9]) == [1, 0]