import math
def square(x):
    square = x * x
    return square
x = float(input("Укажите длину: "))
x = math.ceil(x)
print(math.ceil(square(x)))