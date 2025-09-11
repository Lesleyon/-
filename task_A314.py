 # Написать функцию candy_box(small, big, goal), которая определяет количество конфет, необходимых для 
# составления набора нужного веса (goal). Два типа конфет: вес маленьких конфет - 2, вес больших - 5. 
# На складе доступно small маленьких и big больших.
# Функция должна вернуть список из двух значений: [кол-во маленьких конфет, кол-во больших конфет]. 
# При этом набор должен составляться так, чтобы итоговое кол-во конфет в наборе было минимальным. 
# Если составить набор невозможно, необходимо вернуть [-1, -1]
#  
# Пример
# candy_box(4, 1, 13) ==> [4, 1]  -> 4 * 2 + 1 * 5
# candy_box(4, 1, 14) ==> [-1, -1]  


import traceback


def candy_box(small, big, goal):
    cb = 0
    cs = 0
    if (goal - ((goal // 5) * 5)) % 2 == 0:
        cb = goal // 5
        cs = int((goal - (cb * 5)) / 2)
    else:
        cb = (goal // 5) - 1
        cs = int((goal - (cb * 5)) / 2)
    if (cb == big) and (cs == small):
        return [cs, cb]
    if (goal -((big *5+((small-1)*2)))) == 0:
        cb = big
        cs = (small-1)
        return [cs, cb]
    else:
        if (goal-(small*2)) == 0:
            cb = 0
            cs = small
            return [cs, cb]
        else:
            cb = -1
            cs = -1
            return [cs, cb]
# Тесты
try:
    assert candy_box(4, 1, 13) == [4,1]
    assert candy_box(4, 1, 14) == [-1,-1] 
    assert candy_box(2, 1, 7) == [1,1]
    assert candy_box(3, 1, 6) == [3,0]
    assert candy_box(2, 0, 6) == [-1,-1]
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
