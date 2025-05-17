# bucle_for_basico1.py

# 1. Básico: imprime todos los números enteros del 0 al 100.
print("1. Números del 0 al 100:")
for i in range(101):
    print(i)

# 2. Múltiples de 2 entre 2 y 500
print("\n2. Múltiplos de 2 entre 2 y 500:")
for i in range(2, 501, 2):
    print(i)

# 3. Contando Vanilla Ice
print("\n3. Contando Vanilla Ice:")
for i in range(1, 101):
    if i % 10 == 0:
        print("baby")
    elif i % 5 == 0:
        print("ice ice")
    else:
        print(i)

# 4. Wow. Número gigante a la vista
print("\n4. Suma de números pares del 0 al 500,000:")
suma = 0
for i in range(0, 500001, 2):
    suma += i
print("Suma total:", suma)

# 5. Regrésame al 3
print("\n5. Cuenta regresiva de 2024 al 0 de 3 en 3:")
for i in range(2024, -1, -3):
    print(i)

# 6. Contador dinámico
print("\n6. Contador dinámico:")
numInicial = 3
numFinal = 10
multiplo = 2
for i in range(numInicial, numFinal + 1):
    if i % multiplo == 0:
        print(i)
