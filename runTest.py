#-*- coding:utf-8 –*-
import preprocess
import tree
import evaluation

parties,realSim = preprocess.preprocess(filename='NO_DMV_Match.csv',col=['last_name','first_name','middle_name'],parties=3,corruption=0.4,hashnumber=100,length=1000)

print parties
print realSim
root = tree.createTree(parties,2)
#tree.printTree(root)

clusters = tree.cluster(root)
evaluation.printCluster(clusters)

evaluation.compareAll(clusters,realSim,0.7)
