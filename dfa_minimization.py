from decodificador import decof

url = 'nfa_test'
path = decof(url) [0]
states = decof(url) [1]
mini = {}
ticket = []
no_ticket = []

nums={}
for x in states["Language"]:
    nums[x]= None

def encontrar(x,tuplas):
    for i in tuplas:
        if len(i)>1:
            if x in i:
                return i
        else:
            if x in tuplas:
                return x
    
for i in states["All paths"]:  
    for j in states["All paths"]:
        tupla = (i,j)
        if ((j,i) in mini) or (i == j):
            pass
        else:
            mini[tupla] = "[]"

for i in states["Endn't"]:
    for j in states["End"]:
        tupla = (i,j)
        tupla2 = (j,i)
        if tupla in mini: 
            mini[(i,j)] = "[t]"
        elif tupla2 in mini: 
            mini[(j,i)] = "[t]"      

for i in mini:
    if mini[i] == "[t]":
        ticket.append(i)
    else:
        no_ticket.append(i)
        
i = 0
j = len(no_ticket)
while(i<j):
    j=len(no_ticket)
    for x in states["Language"]:
        if path[no_ticket[i][0]][x][0] in states["End"] and path[no_ticket[i][1]][x][0] in states["Endn't"]:
            mini[no_ticket[i]]= "[t]"
            ticket.append(no_ticket[i])
            no_ticket.pop(i)
            i=-1
        if path[no_ticket[i][1]][x][0] in states["End"] and path[no_ticket[i][0]][x][0] in states ["Endn't"]:
            mini[no_ticket[i]]= "[t]"
            ticket.append(no_ticket[i])
            no_ticket.pop(i)
            i=-1
        elif tuple([path[no_ticket[i][0]][x][0],path[no_ticket[i][1]][x][0]]) in ticket:
            if no_ticket[i] not in ticket:
                mini[no_ticket[i]]= "[t]"
                ticket.append(no_ticket[i])
                no_ticket.pop(i)
                i=-1
            pass
        else:
            pass
    i+=1

similares= {}

for i in states["All paths"]:
    for j in no_ticket:
        if i in j:
            if i not in similares:
                similares[i] = []
                similares[i].append(j)
            elif i in similares:
                similares[i].append(j)

tuplas_d = []
for i in similares:
    lista = []
    if len(similares[i])>1:
        for j in similares[i]:
            j=list(j)
            for x in j:
                if x not in lista:
                    lista.append(x)
                    lista.sort()
        if tuple(lista) not in tuplas_d:
            tuplas_d.append(tuple(lista))
    else:
        if similares[i][0] not in tuplas_d:
            tuplas_d.append((similares[i][0]))

item_tuplas=[]
for j in tuplas_d:
    for i in j:
        if i not in item_tuplas:
            item_tuplas.append(i)     
            
       
for i in states["All paths"]:
    if i not in item_tuplas:    
        tuplas_d.append((i))

final = {}
tuplas=[]
for i in states["All paths"]:
    for j in tuplas_d:
        if len(j)>1:
            if j not in tuplas:
                if i in j:
                    tuplas.insert(len(tuplas),j)
        else:
            if j not in tuplas:
                if i == j:
                    tuplas.insert(len(tuplas),j)

for i in tuplas:
    if len(i)>1:
        i=list(i)
        final[tuple(i)] = path[i[0]]
    else:
        final[i] = path[i]

for i in tuplas:
    dicc = final[i]
    for j in dicc:
        m = encontrar(dicc[j][0],tuplas)
        dicc[j]=m
        
estados = []
e=[]
for x in tuplas:
    if len(x)>1:
        if states["Start"] in x:
            e.append(x)
            x = (f'>{x}')
            estados.append(x)
    else:
        if states["Start"] == x:
            e.append(x)
            x = (f'>{x}')
            estados.append(x)
            
for x in tuplas:
    for y in states["End"]:
        if len(x)>1:
            if y in x:
                e.append(x)
                x=(f'*{x}')
                estados.append(x)
                break
        else:
            if y == x:
                e.append(x)
                x=(f'*{x}')
                estados.append(x)
                break

for i in e:
    if e.count(i) > 1:
        estados.pop(1)
        estados[0] = f'*>{i}'
        break
        
for i in final:
    if i not in e:
        estados.append(i)

new = open(f"dfa_minimization.txt", "w")

new.write("Estados\n")
for x in estados:
    new.write(f'{x}\n')
new.write("Alfabeto\n")
for x in states["Language"]:
    new.write(f'{x}\n')
new.write("Transiciones\n")
for x in final:
    dic = final[x]
    for i in dic:
        new.write(f'{x} {i} -> {dic[i]}\n')
        
new.close()