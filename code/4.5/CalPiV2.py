#蒙特卡洛方法
from random import random
from time import perf_counter
darts=1000*1000
hit=0

start=perf_counter()

for i in range(1,darts+1):
    x,y=random(),random()
    dist=pow(x**2+y**2,0.5)
    if dist<=1:
        hit+=1

pi=4*(hit/darts)
print("圆周率的值为：{}".format(pi))
print("运行时间是：{:.5f}s".format(perf_counter()-start))
