def quicksort(arr):
    # 1. CASO BASE
    # Si la lista está vacía o tiene un solo número, no hay nada que ordenar
    if len(arr) <= 1:
        return arr
    
    # 2. ELEGIR EL PIVOTE
    # Tomamos el elemento del medio como referencia
    indice_mitad = len(arr) // 2
    pivote = arr[indice_mitad]
    
    # 3. CREAR CAJAS (Sub-arrays)
    izquierdos = []   # Números menores al pivote
    iguales = []      # Números iguales al pivote
    derechos = []     # Números mayores al pivote
    
    # 4. REPARTIR LOS NÚMEROS
    for x in arr:
        if x < pivote:
            izquierdos.append(x)
        elif x == pivote:
            iguales.append(x)
        else:
            derechos.append(x)
    
    # 5. RECURSIVIDAD Y UNIÓN
    # Ordenamos las cajas de los lados y pegamos todo en orden
    return quicksort(izquierdos) + iguales + quicksort(derechos)

# Prueba del programa
mi_lista = [38, 27, 43, 3, 9, 82, 10]
resultado = quicksort(mi_lista)

print("Lista original:", mi_lista)
print("Lista ordenada:", resultado)



print("--- PRUEBA DE COBERTURA DE SENTENCIAS ---")


# Caso: Una lista desordenada normal
# Esto obliga al código a calcular el pivote, entrar al for,
# repartir en las 3 listas y hacer la recursión.
entrada = [10, 5, 20]
resultado = quicksort(entrada)


if resultado == [5, 10, 20]:
    print("Prueba PASADA: Se ejecutaron todas las líneas de la función.")
else:
    print("Prueba FALLIDA.")


print("--- PRUEBA DE COBERTURA DE DECISIONES ---")


# 1. Probar la decisión: if len(arr) <= 1
# Camino VERDADERO (Lista vacía)
if quicksort([]) == []:
    print("Decisión 'Lista <= 1' (TRUE): PASADA")


# Camino FALSO (Lista con varios elementos)
if quicksort([5, 2]) == [2, 5]:
    print("Decisión 'Lista <= 1' (FALSE): PASADA")


# 2. Probar las decisiones del bucle FOR (menor, igual, mayor)
# Usamos una lista donde el pivote sea el del medio (5)
# El 3 es menor, el 5 es igual, el 8 es mayor.
entrada_completa = [5, 3, 8]
if quicksort(entrada_completa) == [3, 5, 8]:
    print("Decisiones de comparación (<, ==, >): TODAS PASADAS")