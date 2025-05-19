# wap using python implementation of any arithmetic and quadritic operation
import math
a = 30
b = 5
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
a = 1
b = -3
c = 2
discriminant = b**2 - 4*a*c
root1 = (-b + math.sqrt(discriminant)) / (2*a)
root2 = (-b - math.sqrt(discriminant)) / (2*a)
print("Roots:", root1, root2)