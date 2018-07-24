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
    flag = 0
    for d in data.keys():
        if cluster[d] != getMost(data[d]):

            return 0
    return 1

'''
    Func:
        主函数
    Input:
        LPAData node:[tag1,tag2...]
    @:return
        cluster node1:class1,node2:class2....
'''
def main(mydata):
    data = mydata.copy()
    cluster = dict([(_,_) for _ in data.keys()])
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
def GraphAddEdge(data):
    num=len(data.keys())
    g = Graph(len(data.keys()))
    for d in data.keys():
        for _ in data[d]:
            e_list = g.get_edgelist()
            if (int(d) - 1, int(_) - 1) in e_list or (int(_) - 1, int(d) - 1) in e_list:
                continue
            else:
                g.add_edge(int(d) - 1, int(_) - 1)
    g.vs['label'] = [i for i in range(1, 1+num)]
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
    node_num = len(data.keys())
    g.vs['tag'] = [cluster[str(i)] for i in range(1, 1+node_num)]
    color_s = ['blue', 'pink','green','black','purple']
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



data = loadLpaData('LPAdataset')

g1=GraphAddEdge(data)

plot(g1,margin=20,bbox=(500,500))

cluster=main(data)

g2=GraphAddEdge(data)
g2=GraphColor(g2,cluster)
plot(g2,margin=20,bbox=(500,500))
