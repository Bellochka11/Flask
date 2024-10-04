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

    # Вычисление Y(x)
    Yx = (1 + x ** 2) * math.atan(x) / 2 - x / 2

    # Вычисление S(x)
    S = 0
    n = 1
    while n <= max_n:
        term = ((-1)**(n + 1)) * (x ** (2 * n + 1)) / (4 * n**2 - 1)
        S += term
        n += 1

    print(f"{i + 1:<3} {x:<10.5f} {Yx:<20.10f} {S:<20.10f}")

