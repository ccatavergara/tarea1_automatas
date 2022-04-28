from decodificador import decof

url = 'dfa1'
path = decof(url) [0]
states = decof(url) [1]
mini = {}
ticket = []
no_ticket = []

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
    # print(f"{i} : {mini[i]}") 

print(ticket)
print(no_ticket,'\n')
i = 0
j = len(no_ticket)
while(i<j):
    j=len(no_ticket)
    for x in states["Language"]:
        if path[no_ticket[i][0]][x][0] in states["End"] and path[no_ticket[i][1]][x][0] in states["Endn't"]:
            print(i)
            mini[no_ticket[i]]= "[t]"
            ticket.append(no_ticket[i])
            no_ticket.pop(i)
            i=0
        if path[no_ticket[i][1]][x][0] in states["End"] and path[no_ticket[i][0]][x][0] in states ["Endn't"]:
            mini[no_ticket[i]]= "[t]"
            ticket.append(no_ticket[i])
            no_ticket.pop(i)
            i=0
        elif tuple([path[no_ticket[i][0]][x][0],path[no_ticket[i][1]][x][0]]) in ticket:
            print(no_ticket[i])
            if no_ticket[i] not in ticket:
                mini[no_ticket[i]]= "[t]"
                ticket.append(no_ticket[i])
                no_ticket.pop(i)
                i=-1
            pass
        else:
            pass
    i+=1
print(ticket)
print(no_ticket)
# print("\n"
# )
# print(ticket)
# print(no_ticket)
# print(no_ticket[0])
# print(no_ticket[0][0])
# print(path[no_ticket[0][0]])
# print(path[no_ticket[0][0]][0])
# print(path[no_ticket[0][0]][1][0])

# print("\n"
# )
# for i in mini:
#     print(f"{i} : {mini[i]}") 