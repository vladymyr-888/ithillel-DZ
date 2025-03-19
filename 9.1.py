def popular_words (text, words):
    word_count = {}
    text = text.lower()
    for word in words:
       word_count[word]  =  text.count(word)
       return word_count