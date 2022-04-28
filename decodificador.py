def decof(url):
    data = open(f"{url}.txt","r")
    data_list = data.readlines()
    data.close()
    path = {}

    end=[]
    not_final=[]
    everything=[]
    states={}

    data_type = {'Estados':[], 'Alfabeto':[], 'Transiciones':[]}
    for i in range(len(data_list)):
        data_list[i] = data_list[i].replace("\n", "")

    data_list = list(reversed(data_list))

    temp_data = []

    for i in data_list:
        if i not in data_type:
            temp_data.append(i)
        else:
            data_type[i] = list(reversed(temp_data))
            temp_data = []

    for i in data_type['Estados']:
        est = (i.replace(">", "")).replace("*", "")
        path[est] = {}
        for j in data_type["Alfabeto"]:
            path[est][int(j)] = []

    for i in data_type["Estados"]:
        everything.append(i[-1])
        states["All paths"]=everything
        if '>' in i:
            states["Start"]=i[-1]
        if "*" in i:
            end.append(i[-1])
            states["End"]=end
        else:
            not_final.append(i[-1])
            states["Endn't"] = not_final
    
    for i in data_type["Transiciones"]:
        for j in path[i[0]]:
            if int(i[2]) == j:
                path[i[0]][j].append(i[-1])
    
    states['Language'] = []
    for i in data_type['Alfabeto']:
        states['Language'].append(int(i))

    return [path,states] 