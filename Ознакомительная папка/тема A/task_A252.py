# Написать функцию max_3_sum, которая возвращает наибольшую сумму трех подряд идущих элементов списка.
#
# Пример:
# max_3_sum([1,2,3,4,5]) ==> 12



import traceback


def max_3_sum(arr):
    lst =[]
    while len(lst) < 3:
        max_el = arr.pop(arr.index(max(arr)))
        if max_el not in lst:
            lst.append(max_el)
    print( sum(lst))
    return sum(lst)



# Тесты
try:
    assert max_3_sum([1, 2, 3, 4, 5]) == 12
    assert max_3_sum([20, 10, 30, 20, 10, 15, 30]) == 60
    assert max_3_sum([20, 10, -80, 10, 10, 15, 30]) == 55
    assert max_3_sum([10, -80, -10, -10, 15, -35, 20]) == 0

except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
