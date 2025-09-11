# Н аписать функ  цию max_3_sum, которая возвращает наибольшую сумму трех подряд идущих элементов списка.
#
# Пример:
# max_3_sum([1,2,3,4,5]) ==> 12



import traceback


    

def max_3_sum(arr):
    max_sum = 0
    for i in range (len(arr) - ):
        if ((i+2 < len(arr)) and ((arr[i] + arr[i + 1] + arr[i + 2]) >= max_sum) or (i == 0)):
            max_sum = arr[i] + arr[i + 1] + arr[i + 2]
    print(max_sum)
    return max_sum


# Тесты
try:
    assert max_3_sum([1, 2, 3, 4, 5]) == 12
    assert max_3_sum([10, 10, 30, 20, 10, 15, 30]) == 60
    assert max_3_sum([20, 10, -80, 10, 10, 15, 30]) == 55
    assert max_3_sum([10, -80, -10, -10, 15, -35, 20]) == 0

except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
