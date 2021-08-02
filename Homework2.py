import math

print("Является ли число совершенным?")
print("Введите число:")
a = int(input())
b = 0
for i in range(1, a // 2+1):
    if a % i == 0:
        b += i
if b == a:
    print("Число совершенное")
else:
    print("Число несовершенное")
