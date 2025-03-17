def is_palindrome(text):
    text1 = ''.join(el.lower() for el in text if el.isalnum())
    return text1 == text1[::-1]

assert is_palindrome('A man, a plan, a canal: Panama') == True
assert is_palindrome('0P') == False
assert is_palindrome('a.') == True
assert is_palindrome('aurora') == False
print("ОК")