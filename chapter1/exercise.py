from ecc import FieldElement

print("Programming Bitcoin")

# Exercise 1
a = FieldElement(7, 13)
b = FieldElement(6, 13)
print(a == b)  # False
print(a == a)  # True

print(a != b)  # True
print(a != a)  # False

# Exercise 2
a = FieldElement(7, 13)
b = FieldElement(12, 13)
c = FieldElement(6, 13)
print(a + b == c)  # True

# Exercise 4
prime = 97

print(95 * 45 * 31 % prime)  # 23
print(17 * 13 * 19 * 44 % prime)  # 68
print(12 ** 7 * 77 ** 49 % prime)  # 63

# Exercise 5
prime = 19
k = 1  # 3, 7, 13 and 18 are the other possibilities
# loop through all possible k's 0 up to prime-1
# calculate k*iterator % prime
# Hint - sort!

for k in (1, 3, 7, 13, 18):
    print([k * i % prime for i in range(prime)])

print("Sorted")
for k in (1, 3, 7, 13, 18):
    print(sorted([k * i % prime for i in range(prime)]))

# Exercise 7
# For p = 7, 11, 17, 31, what is this set in  𝐹𝑝 ?
primes = [7, 11, 17, 31, 43]

for prime in (7, 11, 17, 31):
    print([pow(i, prime - 1, prime) for i in range(1, prime)])

# Exercise 8
# Solve the following equations in __F__~31~:
prime = 31
print(3 * pow(24, prime - 2, prime) % prime)
print(pow(17, prime - 4, prime))
print(pow(4, prime - 5, prime) * 11 % prime)
