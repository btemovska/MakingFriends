a = 12
b = 3
print(a + b) #15
print(a - b) #9
print(a * b) #36
print(a / b) #4.0 floating
print(a // b ) #4 integer division, rounded down towards minus infinity
print(a % b) #0 modulo: the remainder after integer division

print()
for i in range(1,4):
    print(i)  #1 2 3

print()
for z in range(1, a // b):
    print(z) #1 2 3

print()
print()
#operating presidence
print(a + b / 3 - 4 * 12) #-35.0
print(a + (b / 3) - (4 * 12)) #-35.0
print((((a + b) / 3) - 4) *12 ) #12.0
print(((a + b ) / 3 - 4 ) * 12) #12.0

c = a + b
d = c / 3
e = d - 4
print(e * 12)

print()

print(a / (b * a) / b) #0.1111111111111111