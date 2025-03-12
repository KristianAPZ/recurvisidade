def somarLista(lista):
    if not lista:
        return 0
    else:
        return lista[0] + somarLista(lista[1:])


print(somarLista([7, 5, 3, 4, 1]))
