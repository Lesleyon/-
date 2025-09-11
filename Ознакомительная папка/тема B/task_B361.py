# Написать функцию morse, которая расшифровывает строку, закодированную азбукой Морзе
# a .-      h ....    o ---     u ..-      1 .----     6 -....
# b -...    i ..      p .--.    v ...-     2 ..---     7 --...
# c -.-.    j .---    q --.-    w .--      3 ...--     8 ---..
# d -..     k -.-     r .-.     x -..-     4 ....-     9 ----.
# e .       l .-..    s ...     y -.--     5 .....     0 -----
# f ..-.    m --      t -       z --..
# g --.     n -.
#
# Пример:
# morse("..  .- --  .-  - . ... -") ==> "i am a test"


import traceback


def morse(text):
    # Тело функции
    return ""


# Тесты
try:
    assert morse(".... . .-.. .-.. ---  .-- --- .-. .-.. -..") == "hello world"
    assert morse(".---- ... -  .- -. -..  ..--- -. -..") == "1st and 2nd"
    assert morse(".- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --.. ----- .---- ..--- ...-- ....- ..... -.... --... ---.. ----.") \
        == "abcdefghijklmnopqrstuvwxyz0123456789"
    assert morse("") == ""
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
