data = open("nfa4.txt","r")
data_list = data.readlines()
data.close()
path = {}

data_type = {'Estados':[], 'Alfabeto':[], 'Transiciones':[]}
for i in range(len(data_list)):
    data_list[i] = data_list[i][:-1]

data_list = list(reversed(data_list))

temp_data = []

for i in data_list:
    if i not in data_type:
        temp_data.append(i)
    else:
        data_type[i] = list(reversed(temp_data))
        temp_data = []

for i in data_type["Transiciones"]:
    if i[0] not in path:
        path[i[0]] = {}
    for j in data_type["Alfabeto"]:
        path[i[0]][int(j)] = []

print(path)
print(data_type)


for i in data_type["Transiciones"]:
    for j in path[i[0]]:
        if int(i[2]) == j:
            path[i[0]][j].append(i[-1])

print(path)