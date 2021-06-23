"""
Создала функцию, котрая запрашивает у пользователя число на английском. Если пользователь ввел
число с большой буквы, для корректной работы функции я привожу его к нижнему регистру.
Далле, при помощи get, нахожу значение по ключу и возвращаю значение на русском с большой буквы,
как запрашивается в условиях задачи. Если число передано с маленькой буквы - возвращаю перевод.
"""


def num_translate():
    dictionary = {
        'zero': 'ноль',
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять'
    }

    word = input('Введите число от 0 до 10 английском: ')
    if word.istitle():
        answer = str(dictionary.get(word.lower()))
        return answer.capitalize()
    return dictionary.get(word)


print(num_translate())


