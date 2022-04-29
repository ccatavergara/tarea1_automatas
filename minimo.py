from decodificador import decof

url = 'dfa_input'
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
            if x in tupla:
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

print(ticket)
print(no_ticket,'\n')
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
    
    
fijo = []

print(ticket)
print(no_ticket,'\n')

similares= {}

for i in states["All paths"]:
    for j in no_ticket:
        if i in j:
            if i not in similares:
                similares[i] = []
                similares[i].append(j)
            elif i in similares:
                similares[i].append(j)

tuplas = []
for i in similares:
    lista = []
    if len(similares[i])>1:
        for j in similares[i]:
            j=list(j)
            for x in j:
                if x not in lista:
                    lista.append(x)
                    lista.sort()
        if tuple(lista) not in tuplas:
            tuplas.append(tuple(lista))
    else:
        if similares[i][0] not in tuplas:
            tuplas.append((similares[i][0]))

item_tuplas=[]
for j in tuplas:
    for i in j:
        if i not in item_tuplas:
            item_tuplas.append(i)     
            
       
for i in states["All paths"]:
    if i not in item_tuplas:    
        tuplas.append((i))

final = {}

for i in tuplas:
    if len(i)>1:
        i=list(i)
        final[tuple(i)] = path[i[0]]
    else:
        final[i] = path[i]

for i in tuplas:
    dic = final[i]
    for j in dic:
        m = encontrar(dic[j][0],tuplas)
        dic[j]=m
        
print(final)
