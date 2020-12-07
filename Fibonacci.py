
x = 0
y = 1
result = 0

limit = int(input("Cantidad de elementos de la sucecion de Fibonacci"))

print(x)
print(y)

plus = lambda val1 = 0, val2 = 0: val1 + val2
operation = lambda operation, val1 = 0, val2 = 0 : operation(val1, val2)

for i in range(limit - 2):
    result = operation(plus, x, y) 
    print(result)
    x = y
    y = result
print()