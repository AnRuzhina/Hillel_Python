# Визначити популярність певних слів у тексті

def popular_words(text, words):
    text = text.lower()
    word_list = text.split()
    word_count = {word: word_list.count(word) for word in words}

    return word_count


result = popular_words(text=input(), words=['i', 'was', 'three', 'near'])
print(result)


assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''',
                     ['i', 'was', 'three', 'near']) == {'i': 4, 'was': 3, 'three': 0, 'near': 0}, 'Test1'
print('OK')
