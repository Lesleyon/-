import traceback
import math
def funk_z(funk_k):
    x1 = funk_k()
    k3 = funk_k()
    z = math.pow(math.e, math.sin(k3*math.pow(x1,3))) - math.pow(math.fabs(math.sin(x1)),1/3)
    print (z)
    return z
def funk_k():
    x = 45
    y = 45
    c = 1/math.e
    a1 =  math.pow(c, 2) + 0.83
    a2 = math.pow(x , 2)
    a = a1/a2
    k1 = (math.pow(math.cos(x), 2) + math.pow(math.sin(y), 2))
    k21 = (math.pow(x,2)*a) - 0.82
    k22  = math.log(math.sqrt(k21))
    k2 = 1 + k22
    k = k1/k2
    print (k)
    return k
