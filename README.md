# Label-Propagation
## Introduction
  LPA算法的基本思想是为网络中所有的节点赋予不同的标签，设计一个传播规则，标签根据这个规则在网络上迭代传播，直到所有节点的标签传播达到稳定，最后将具有相同标签的节点划分到一个社区中。在每次迭代传播时，每个节点的标签都更新为最多数量的邻居节点拥有的标签。这个传播规则定义了网络的社区结构，即网络中每个节点选择加入的社区是它最多数量的邻居节点属于的社区。<br>
  Label Propagation is a randomized community detection algorithm, it gives a large number of small sized clusters. It is a useful benchmark. <br>
This repository implements LPA with `Python` and import `igraph` as visualization.
## Operation Environment
- python-igraph
## Data Input
- data
 We get some football match data like this.<br>
 **All the groups are number**
 ```
 group1 g2,g3,g4...
 group2 g1,g3....
 ...
 ```
- label
 We have some label like this.<br>
 ```
 0,missipi
 1,fox
 ...
 ```
 **IT MUST START WITH 0**
 
 ## Data Ouput
 You will see two graph running this code.<br>
 The first graph is the nodes before classification.<br>
 ![image](https://github.com/TerenceLiu2/Label-Propagation-LPA-/blob/master/Img/igraphv_QvzI.png)<br>
 The second is after the classfication.<br>
 ![image](https://github.com/TerenceLiu2/Label-Propagation-LPA-/blob/master/Img/igraphaoLkvj.png)<br>
 What's more, the `cluster` data will offer.
 ## Operation Instruction
 Prepare some datas,then run `Main.py`
