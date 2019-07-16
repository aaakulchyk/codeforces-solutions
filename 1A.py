import math


n, m, a = [int(i) for i in input().split()]
w = math.ceil(n / a)
h = math.ceil(m / a)
print(w * h)
