# Список із 3 елементів
import random

a = [random.randint(1, 100) for i in range(random.randint(3, 10))]
b = [a[0], a[2], a[-2]]
print(a)
print(b)
