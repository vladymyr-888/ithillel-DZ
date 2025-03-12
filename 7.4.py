def common_elements():
    a = set(range(3, 100, 3))
    b = set(range(5, 100, 5))
    c = a.intersection(b)
    return c
print(common_elements())