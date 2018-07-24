# Label-Propagation
## Introduction
  LPA算法的基本思想是为网络中所有的节点赋予不同的标签，设计一个传播规则，标签根据这个规则在网络上迭代传播，直到所有节点的标签传播达到稳定，最后将具有相同标签的节点划分到一个社区中。在每次迭代传播时，每个节点的标签都更新为最多数量的邻居节点拥有的标签。这个传播规则定义了网络的社区结构，即网络中每个节点选择加入的社区是它最多数量的邻居节点属于的社区。<br>
  Label Propagation is a randomized community detection algorithm, it gives a large number of small sized clusters. It is a useful benchmark. <br>
This repository implements LPA with `Python` and import `igraph` as visualization.
## Operation Environment
- python-igraph
## Data Input
 Node-Edge Information -- LPAdataset in this repository is an example. <br>
 The data structure is
 ```
 node1  node2,node3,node4
 node2  node1,node3
 node3  node2,node1
 node4  node1
 ```
 **NAME MUST BE A NUMBER**
 ## Data Ouput
 You will see two graph running this code.<br>
 The first graph is the nodes before classification.<br>
 ![image](https://github.com/TerenceLiu2/Label-Propagation-LPA-/blob/master/Img/igraphgTX0Pl.png)<br>
 The second is after the classfication.<br>
 ![image](https://github.com/TerenceLiu2/Label-Propagation-LPA-/blob/master/Img/igraphrHV9mk.png)<br>
 What's more, the `cluster` data will offer.
 ## Operation Instruction
 Prepare some datas,then run `Main.py`
