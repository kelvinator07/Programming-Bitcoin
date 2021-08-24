# Specifically, the elliptic curve used in Bitcoin is called secp256k1 and it uses this particular
# equation:
# y2 = x3 + 7
# The canonical form is y2 = x3 + ax + b, so the curve is defined by the constants a = 0, b = 7.
from ecc import Point

p1 = Point(-1, -1, 5, 7)


# p2 = Point(-1, -2, 5, 7) Error, Not On The Curve


# Exercise 1
# (2,4), (-1,-1), (18,77), (5,7)
# equation in python is: y**2 == x**3 + 5*x + 7
def on_curve(x, y):
    return y ** 2 == x ** 3 + 5 * x + 7


print(on_curve(2, 4))  # False
print(on_curve(-1, -1))  # True
print(on_curve(18, 77))  # True
print(on_curve(5, 7))  # False

# Exercise 4
# For the curve __y__^2^ = __x__^3^ + 5__x__ + 7, what is (2,5) + (–1,–1)?
x1, y1 = 2, 5
x2, y2 = -1, -1
s = (y2 - y1) / (x2 - x1)
x3 = s ** 2 - x1 - x2
y3 = s * (x1 - x3) - y1
print(x3, y3)  # 3.0 -7.0

# Exercise 6
# For the curve __y__^2^ = __x__^3^ + 5__x__ + 7, what is (–1,–1) + (–1,–1)?
a, x1, y1 = 5, -1, -1
s = (3 * x1 ** 2 + a) / (2 * y1)
x3 = s ** 2 - 2 * x1
y3 = s * (x1 - x3) - y1
print(x3, y3)  # 18.0 77.0
