

info_dict={}

with open("football_data.csv") as f:
    lines=f.readlines()
    for line in lines:
        line=line.replace('\n','')
        if info_dict.has_key(line.split(',')[0]):
            info_dict[line.split(',')[0]].append(line.split(',')[1])
        else:
            info_dict[line.split(',')[0]]=[line.split(',')[1]]
        if info_dict.has_key(line.split(',')[1]):
            info_dict[line.split(',')[1]].append(line.split(',')[0])
        else:
            info_dict[line.split(',')[1]]=[line.split(',')[0]]

with open('dataset','a') as wf:
    for key in info_dict.keys():
        wStr=key+'\t'
        for i in info_dict[key]:
            wStr+=i+','
        wStr+='\n'
        wStr=wStr.replace(',\n','\n')
        wf.write(wStr)