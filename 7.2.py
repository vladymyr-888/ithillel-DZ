def correct_sentence(text):
    text = text.capitalize()
    if not text.endswith('.'):
        text += '.'
    return text
print(correct_sentence('hello Vika'))
print(correct_sentence('hello Vika.'))