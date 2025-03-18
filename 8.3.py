def find_unique_value(some_list):
    unique_values = set()
    for number in some_list:
        if number in unique_values:
            unique_values.remove(number)
        else:
            unique_values.add(number)
    return unique_values.pop()
print(find_unique_value([2, 3, 3, 3, 5, 5]))