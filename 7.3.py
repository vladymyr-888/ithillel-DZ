def second_index(text, some_str):
    first_index = text.find(some_str)
    second_index = text.find(some_str,first_index +1)
    if second_index < 1:
        print('None')
    else:return second_index

print(second_index('morozko', 'o'))