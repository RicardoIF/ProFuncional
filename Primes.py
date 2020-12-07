limit = int(input("Hasta donde desea contar? "))

plus = lambda val1 = 0, val2 = 0: val1 + val2
operation = lambda operation, val1 = 0, val2 = 0: operation(val1, val2)  
counter = 0
val = 1
for i in range(limit):
    if i%2 == 0:
        counter = operation(plus, counter, val)
print()

print("Desde", 0, "hasta", limit, "hay", counter, "numeros primos.")

