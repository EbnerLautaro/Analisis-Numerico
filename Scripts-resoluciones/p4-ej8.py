import math

x_y: list[tuple[float, float]] = [
    (0, 1.8),
    (1, 3.5),
    (2, 2.1),
    (3, -1),
    (4, -3.3),
    (5, -2.7),
    (6, 0.9),
    (7, 3.3),
    (8, 2.8),
    (9, -0.1),
    (10, -3),
]


cos_2 = 0
sincos = 0
sin_2 = 0
yicos = 0
yisin = 0

for xi, yi in x_y:
    cos_2 += math.cos(xi) ** 2
    sincos += math.sin(xi) * math.cos(xi)
    sin_2 += math.sin(xi) ** 2
    yicos += yi * math.cos(xi)
    yisin += yi * math.sin(xi)

print(f"cos^2(x) = {cos_2}")
print(f"sen(x)cos(x) = {sincos}")
print(f"sen^2(x) = {sin_2}")
print(f"yi*cos(x) = {yicos}")
print(f"yi*sen(x) = {yisin}")
