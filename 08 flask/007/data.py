def operacion(data):
    lista = []
    for f in data:
        lista.append((f[0],suma(f[1:])))
    return lista

def suma(lista):
    if lista==[]:
        return 0
    return int(lista[0])+suma(lista[1:])