#task1
from functools import reduce
from operator import mul
a = list(map(int,input().split()))
res = reduce(mul,a)
print(res)

#task2
a = input()
cnt = sum(1 for i in a if i.islower() )
cnt1 = sum(1 for i in a if i.isupper() )
print(f"lower: {cnt} \nupper: {cnt1}")

#task3
a = input()
g = reversed(a)
res = "".join(g)
if res == a:
    print("yeeeep")
else:
    print("cryyy")

#task4
import time
import math
b = int(input())
a = int(input())
time.sleep(a//1000)
print(math.sqrt(b))

#task5
a = tuple(map(int,(input()).split()))
res = all(a)
print(res)

