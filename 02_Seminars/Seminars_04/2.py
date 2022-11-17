# Найдите корни квадратного уравнения Ax² + Bx + C = 0
# Ввод: A, B, C
# D = B^2 - 4*A*C

# x = -D/(2*A)

# x1 = (-b + sqrt(D)) / 2 * a
# x2 = (-b - sqrt(D)) / 2 * a

a = int(input("Ввидите А: "))
b = int(input("Ввидите B: "))
c = int(input("Ввидите C: "))

d = b**2 - 4*a*c
if d > 0:
    x1 = (-b + d**0.5) / (2 * a)
    x2 = (-b - d**0.5) / (2 * a)
    print(f"x1 = {x1}")
    print(f"x2 = {x2}")
elif d == 0:
    x = -b / (2 * a)
    print(f"x = {x}")
elif d < 0:
    print("Действительных корней нет")