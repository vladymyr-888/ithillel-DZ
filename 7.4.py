def common_elements():
    a = set(range(0, 100, 3))
    b = set(range(0, 100, 5))
    c = a.intersection(b)
    return c
print(common_elements())

assert common_elements() == {0, 75, 45, 15, 90, 60, 30}