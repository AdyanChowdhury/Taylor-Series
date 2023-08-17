import math as m
sum = 0
angle = 37
factorial = 0
radian = (angle + m.pi) / 180

for i in range(0, 60):
    sum = sum + (((-1) ** i * radian ** (2 * i)) / m.factorial(2 * i))

print(sum)
