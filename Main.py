#coding=utf8
from igraph import *


'''
    Func:
        读取数据
    DataStructure:
        n1,e1,e2
        n2,e1,e2
        ...
    @:return node:[tag1,tag2...]
'''
def loadLpaData(filename):
    f = open(filename, 'r')
    data = {}
    for i in f.readlines():
        order, ship = i.split()[0], i.split()[1]
        ships = ship.split(',')
        #Set k-v
        data.setdefault(order, ships)
    f.close()
    return data


'''
    Func:
        选出邻居中最大的tag
    Input：
        邻居tag列表 [tag1,tag2...]
    @:return 返回邻居最大的tag tagMax
'''
def getMost(ships):

    import collections
    #求和邻居tag
    counter = collections.Counter(ships)
    #排序邻居tag
    tmp = sorted(counter.items(), key=lambda x: x[1])

    #选出最大的邻居tag
    maxc = tmp[-1][1]
    maxset = []
    for i in tmp:
        if i[1] == maxc: maxset.append(i[0])

    #random choice
    import random
    random.shuffle(maxset)
    return maxset[0]

'''
    Func:
        更新邻居表
    Input:
        node:tag (seq)
        node:tag1,tag2 (seq)
'''
def updateShips(cluster,data):
    for _ in data.keys():
        data[_] = [cluster[i] for i in data[_]]

'''
    Func:
        判断是否收敛
    Input:
        node:tag (seq)  
        node:tag1,tag2 (seq)
    @:return 1 -- True 2 -- False
'''
def checkStatus(cluster,data):
    for d in data.keys():
        if cluster[d] != getMost(data[d]):
            return 0
    return 1

'''
    Func:
        主函数
    Input:
        LPAData node:[tag1,tag2...]
        node num
    @:return
        cluster node1:class1,node2:class2....
'''
def main(mydata,num):
    data = mydata.copy()
    cluster = dict([(str(_),str(_)) for _ in range(num)])
    #Initial tag
    while 1:
        if checkStatus(cluster,data):break
        for i in cluster.keys():
            cluster[i] = getMost(data[i])
            updateShips(cluster,data)
    return cluster

'''
    Func:
        绘制无向图
    Input:
        LPAData node:[tag1,tag2...]
        node_num
    Output:
        Graph with edges and label
'''
def GraphAddEdge(data,num):
    g = Graph(num)
    key_list=labeldict.keys()
    for i in  range(num):
        g.vs[i]['no']=key_list[i]
        g.vs[i]['name'] = labeldict[key_list[i]]
        g.vs[i]['label']=g.vs[i]['name']
    for d in data.keys():
        # print g.vs.select(no=d)[0].index
        for _ in data[d]:
            e_list = g.get_edgelist()
            if (g.vs.select(no=d)[0].index, g.vs.select(no=_)[0].index) in e_list or (g.vs.select(no=_)[0].index, g.vs.select(no=d)[0].index) in e_list:
                continue
            else:
                g.add_edge(g.vs.select(no=d)[0], g.vs.select(no=_)[0])
    return g

'''
    Func:
        根据分类情况添加颜色
    Input:
        Graph
        cluster str(n1):c1,n2:c2
        node_num
    @:return
        Graph with color
'''
def GraphColor(g,cluster):
    for vs in g.vs:
        vs['tag']=cluster[vs['no']]
    color_s = ['blue', 'pink','green','black','purple','orange','brown','yellow','gold']
    color_l = []
    tmp = {g.vs['tag'][0]: 'red'}
    cot = -1
    for t in g.vs['tag']:
        if t not in tmp.keys():
            cot += 1
            tmp[t] = color_s[cot]
        color_l.append(tmp[t])
    g.vs['color'] = color_l
    return g

'''
    Func:
        提取label字典
    Input：
        Label文件
        0,l1
        1,l2
    Output:
        label字典
'''
def LabelDict(labelname):
    f = open(labelname, 'r')
    data = {}
    for i in f.readlines():
        no, name = i.split(',')
        data[no]=name.replace('\r\n','')
    f.close()
    return data

num=115
data = loadLpaData('data/football_data')
labeldict=LabelDict('data/football_label.csv')


g1=GraphAddEdge(data,num)
plot(g1,margin=20,bbox=(1000,1000))

cluster=main(data,num)
print cluster

g2=GraphAddEdge(data,num)
g2=GraphColor(g2,cluster,num)
plot(g2,margin=20,bbox=(1000,1000))
