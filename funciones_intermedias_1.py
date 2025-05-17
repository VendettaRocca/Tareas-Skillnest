# funciones_intermedias_1.py

# 1. Actualizar valores en diccionarios y listas

matriz = [ [10, 15, 20], [3, 7, 14] ]
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"}
]
ciudades = {
    "México": ["Ciudad de México", "Guadalajara", "Cancún"],
    "Chile": ["Santiago", "Concepción", "Viña del Mar"]
}
coordenadas = [
    {"latitud": 8.2588997, "longitud": -84.9399704}
]

# Cambiar el 3 por 6 en matriz
matriz[1][0] = 6

# Cambiar el nombre del primer cantante
cantantes[0]["nombre"] = "Enrique Martin Morales"

# Cambiar "Cancún" por "Monterrey"
ciudades["México"][2] = "Monterrey"

# Cambiar latitud a 9.9355431
coordenadas[0]["latitud"] = 9.9355431

# 2. Iterar a través de una lista de diccionarios

def iterarDiccionario(lista):
    for dic in lista:
        # Para el bonus en formato: key - value, key - value
        salida = []
        for llave, valor in dic.items():
            salida.append(f"{llave} - {valor}")
        print(", ".join(salida))


# 3. Obtener valores de una lista de diccionarios

def iterarDiccionario2(llave, lista):
    for dic in lista:
        if llave in dic:
            print(dic[llave])


# 4. Iterar a través de un diccionario con valores de lista

def imprimirInformacion(diccionario):
    for clave, lista_valores in diccionario.items():
        print(f"{len(lista_valores)} {clave.upper()}")
        for valor in lista_valores:
            print(valor)
        print()  # línea en blanco para separar secciones


# Código de prueba 

if __name__ == "__main__":
    print("Matriz actualizada:", matriz)
    print("Cantantes actualizados:", cantantes)
    print("Ciudades actualizadas:", ciudades)
    print("Coordenadas actualizadas:", coordenadas)
    print("\nIterar Diccionario:")
    cantantes_prueba = [
        {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
        {"nombre": "Chayanne", "pais": "Puerto Rico"},
        {"nombre": "José José", "pais": "México"},
        {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
    ]
    iterarDiccionario(cantantes_prueba)

    print("\nIterar Diccionario 2 (nombres):")
    iterarDiccionario2("nombre", cantantes_prueba)

    print("\nIterar Diccionario 2 (países):")
    iterarDiccionario2("pais", cantantes_prueba)

    print("\nImprimir Información:")
    costa_rica = {
        "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
        "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
    }
    imprimirInformacion(costa_rica)
