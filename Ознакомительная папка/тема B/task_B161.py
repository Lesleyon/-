# Написать функцию valid_ISBN10, которая получает строку (ISBN-номер) и проверяет ее на правильность. 
# ISBN-номер состоит из 10 знаков, Первые девять - цифры от 0 до 9. Последний знак - цифры от 0 до 9 или 'X' для обозначения 10.
# ISBN-номер валидный, если сумма произведений цифр на их позицию, взятая по остатку от деления на 11 дает 0.
#
# Примеры:
# valid_ISBN10('1112223339') ==> True 
# 
# ISBN     : 1 1 1 2 2 2 3 3 3  9
# позиция  : 1 2 3 4 5 6 7 8 9 10
# (1*1 + 1*2 + 1*3 + 2*4 + 2*5 + 2*6 + 3*7 + 3*8 + 3*9 + 9*10) % 11 = 0 ==> True

import traceback


def valid_ISBN10(isbn):
    check_digit = int(isbn[-1])
    match = re.search(r'(\d)-(\d{3})-(\d{5})', isbn[:-1])

    if not match:
        return False

    digits = match.group(1) + match.group(2) + match.group(3)
    result = 0

    for i, digit in enumerate(digits):
      result += (i + 1) * int(digit)

    return True if (result % 11) == check_digit else False


# Тесты
try:
    assert valid_ISBN10('1112223339') == True
    assert valid_ISBN10('048665088X') == True
    assert valid_ISBN10('1293000000') == True
    assert valid_ISBN10('1234554321') == True
    assert valid_ISBN10('1234512345') == False
    assert valid_ISBN10('1293') == False
    assert valid_ISBN10('X123456788') == False
    assert valid_ISBN10('ABCDEFGHIJ') == False
    assert valid_ISBN10('XXXXXXXXXX') == False    
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
