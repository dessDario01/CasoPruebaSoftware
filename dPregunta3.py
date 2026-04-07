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
