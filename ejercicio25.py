from math import sqrt

a = int(input('Ingresa el valor de a: '))
b = int(input('Ingresa el valor de b: '))
c = int(input('Ingresa el valor de c: '))
root1 = -b + sqrt(b ** 2 - 4 * a * c) / (2 * a)
root2 = -b - sqrt(b ** 2 - 4 * a * c) / (2 * a)


print(root1)
print(root2)