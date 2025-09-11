# Дана строка, написать функцию last, которая возвращает список слов этого предложения,
# отсортировав их в алфавитном порядке по последнему символу
#
# Пример:
# last("i love python") ==> ["love", "i", "python"]


import traceback


def last(s):
    print(sorted(s.split(), key=lambda x: x[-1]))
    return [sorted(s.split(), key=lambda x: x[-1])
]


# Тесты
try:
    assert last("man i need a taxi up to ubud") == ["a", "need", "ubud", "i", "taxi", "man", "to", "up"]
    assert last("what time are we climbing up the volcano") == ["time", "are", "we", "the", "climbing", "volcano", "up", "what"]
    assert last("massage yes massage yes massage") == ["massage", "massage", "massage", "yes", "yes"]
    assert last("i love python") == ["love", "i", "python"]
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
