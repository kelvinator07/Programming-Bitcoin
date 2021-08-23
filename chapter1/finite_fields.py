from ecc import FieldElement

#
a = FieldElement(7, 13)
b = FieldElement(6, 13)
print(a == b)  # False
print(a == a)  # True

#
print(a != b)  # True
print(a != a)  # False

#  f57 a + b = (a + b) % 57 = ?
#  f57 44 + 33 = 77 % 57 = 20
#  f57 9 - 29 = - 20 % 57 = 37
#  f57 17 + 42 + 49 = 108 % 57 = 51
#  f57 52 - 30 - 38 = -16 % 57 = 41

print(77 % 57)
print(20 % 57)
print(108 % 57)
print(-16 % 57)

#
a = FieldElement(3, 13)
b = FieldElement(12, 13)
c = FieldElement(10, 13)
print(a * b == c)
