import math

x_start = 0.1
x_end = 1.0
num_points = 30
epsilon = 1e-5
max_n = 100
dx = (x_end - x_start) / (num_points - 1)

print(f"{'N':<3} {'X':<10} {'Y(X)':<20} {'S(X)':<20}")

for i in range(num_points):
    x = x_start + i * dx

    Yx = (1 + x ** 2) * math.atan(x) / 2 - x / 2

    # Вычисление S(x) с использованием рекуррентных множителей
    S1 = 0
    S2 = 0

    for n in range(1, max_n + 1):
        # Первый ряд, избегаем деления на ноль
        if n > 1:
            an = (-1)**(n + 1)  # Коэффициент для первого ряда
            S1 += (an * math.sin(n * x)) / (n**2 - 1)

        # Второй ряд
        if n > 1:  # Учитываем n(n-1) только для n > 1
            a = (-S2 * x**2) / (n * (n - 1))
            S2 += a

    S = S1 + S2  # Общая сумма

    print(f"{i + 1:<3} {x:<10.5f} {Yx:<20.10f} {S:<20.10f}")
