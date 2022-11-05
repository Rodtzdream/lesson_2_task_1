import random
N, r = 0, 65536
for i in range(100000):
    x = random.uniform(-65536, 65536)
    y = random.uniform(-65536, 65536)
    if(x*x + y*y <= r * r):
        N += 1
print(4 * N / 100000);