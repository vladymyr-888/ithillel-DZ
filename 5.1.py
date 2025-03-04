import keyword
import string


name = input("Введіть ім'я змінної: ")
if name in keyword.kwlist:
    print(False)
elif name[0].isdigit():
    print(False)
elif any(element.isupper() for element in name):
    print(False)
elif any(element in string.punctuation for element in name ) and not(element == '_' for element in name):
    print(False)
elif name.count('_') > 1:
    print(False)
else:
    print(True)