sum = 0
for i in range(1, 6):
    next_val = 2*i - 1
    sum = next_val + sum
print(sum)

for i in range(1, 11):
    print(i **2)
    sum = sum + i**2

print("sum of all values", sum)
