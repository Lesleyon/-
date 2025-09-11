# Написать функцию max_3_sum, которая возвращает наибольшую сумму трех подряд идущих элементов списка.
#
# Пример:
# max_3_sum([1,2,3,4,5]) ==> 12



import traceback


def max_3_sum(arr):
    length = len(arr)

    n = 0
    while n < length:
        m = n
        if m < length:
            first = arr[n]
        if m+1 < length:
            second = arr[m+1]
        else:
            second = 0
        if m+2 < length:
            third = arr[m+2]
        else:
            third = 0
        result = first + second + third
        n = n+1
    print (result)
    return result


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
