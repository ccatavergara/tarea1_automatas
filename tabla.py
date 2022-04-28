from decodificador import decof

url = 'nfa4'
path = decof(url) [0]
states = decof(url) [1]
start = states['Start']

def agregar(lista):
    if len(lista) == 0:
        if '' not in tabla:
            tabla[''] = numbs
    if len(lista) == 1:
        if lista[0] not in tabla:
            tabla[lista[0]] = numbs
    elif len(lista)>=1:
        tupla=tuple(lista)
        if tupla not in tabla:
            tabla[tupla] = numbs


tabla = {}
numbs = {}
for i in path[start]:
    numbs[i] = ""

tabla[start] = path[start]
trans = []
for i in tabla[start]:
    trans.append(i)

for i in tabla[start]:
    lista = tabla[start][i]
    agregar(lista)

print(tabla)
for i in tabla:
    if len(i) == 1:
        for x in tabla[i]:
            lista = tabla[i][x]
            agregar(lista)
    if len(i) >= 1:
        for j in i:
            lista=j
            agregar(lista)

print(tabla)