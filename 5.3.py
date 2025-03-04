import string
text = input('Enter text')
words = text.split()
word = ''.join([char for char in words if char  not in  string.punctuation and char != ' '])
hashtag = '#' + ''.join(word.capitalize() for word in words)
if len(hashtag) > 140:
    hashtag = hashtag[:140]
print(hashtag)