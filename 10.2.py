import string


def first_word(text):
    """ Пошук першого слова """
    word = text.strip(string.punctuation).split()
    return word[0].strip(string.punctuation)
