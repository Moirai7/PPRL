#-*- coding:utf-8 –*-
import getBestBit

'''
树上面的结点
'''
class TreeNode:
    def __init__(self,idx):
	self.idx = idx
    def set_idx(self,idx):
	self.idx = idx
    def set_left(self,left):
	self.left = left
    def set_right(self,right):
	self.right = right
    def get_idx(self):
         return self.idx
    def get_left(self):
	return self.left
    def get_right(self):
	return self.right    	
'''
叶子结点
'''
class LeafNode:
    def __init__(self,idx):
	self.idx = idx
    def set_idx(self,idx):
	self.idx = idx
    def set_nextIdx(self,nextidx):
	self.nextidx = nextidx
    def set_value(self,value):
	self.value = value
    def get_nextIdx(self):
	return self.nextidx
    def get_idx(self):
        return self.idx
    def get_value(self):
	return self.value
'''
添加树
递归
'''
def addTree(root,parties,minBucket):
	p_ratio = getBestBit.generateRatios(parties,alpha=0.5)
	sums = getBestBit.secureSummation(p_ratio)
	rootid = getBestBit.getBestBit(sums)
	left = []
	right = []
        check_left = False
        check_right = False
        for i in xrange(len(parties)):
		p = parties[i]
                _left = p[p.iloc[:,rootid]==1]
                _right = p[p.iloc[:,rootid]==0]
                left.append(_left)
                right.append(_right)
		'''
		print 'right'
                for index,r in _right.iterrows():
                        print index
                print 'left'
                for index,r in _left.iterrows():
                        print index
		'''
                if len(_left)>minBucket:
                        check_left = True
                if len(_right)>minBucket:
                        check_right = True
                p.loc[:,rootid] = 1
		p.loc[:,rootid] = 1
		root[i].set_idx(rootid)
	
	if check_left:
		_temp = []
		for i in xrange(len(parties)):
			t = TreeNode(-1)
			_temp.append(t)
			root[i].set_left(t)
		addTree(_temp,left,minBucket)
	else:
		for i in xrange(len(parties)):
			root[i].set_left(LeafNode(-1))
			addLeaf(root[i].get_left(),left[i])
	if check_right:
		_temp = []
		for i in xrange(len(parties)):
			t = TreeNode(-1)
			_temp.append(t)
			root[i].set_right(t)
                addTree(_temp,right,minBucket)
	else:
		for i in xrange(len(parties)):
			root[i].set_right(LeafNode(-1))
			addLeaf(root[i].get_right(),right[i])
'''
添加叶子
递归
'''
def addLeaf(node, data):
	for index, row in data.iterrows(): 
		#node.set_idx('m'+str(index))
		node.set_idx(str(index))
		node.set_value(row)
		node.set_nextIdx(LeafNode(-1))
		node = node.get_nextIdx();
'''
打印
'''
def printNode(node):
	if node.get_idx()!=-1:
		if isinstance(node, LeafNode):
			print 'idx: m' + str(node.get_idx())
			print str(node.get_idx()), 'nextidx: ',
			printNode(node.get_nextIdx())
		else:
			print 'idx: ' + str(node.get_idx())
			print str(node.get_idx()), 'left: ',
			printNode(node.get_left())
			print str(node.get_idx()), 'right: ',
			printNode(node.get_right())
	else:
		print 'end'
'''
打印
'''
def printTree(rootnode):
	for root in rootnode:
		printNode(root)
'''
创建树
minbucket是论文中的max
'''
def createTree(parties,minBucket):
	root = []
	for p in parties:
		root.append(TreeNode(-1))
	addTree(root,parties,minBucket)
	return root
'''
'''
def saveLeaf(node,_temp):
	if node.get_idx()!=-1 :
		#_temp.append((node.get_idx(),node.get_value()))
		#_temp.append(node.get_value())
		_temp[node.get_idx()]=node.get_value();
		saveLeaf(node.get_nextIdx(),_temp)
'''
'''
def searchLeaf(node,result):
	if node.get_idx()!=-1 :
		if isinstance(node, LeafNode):
			_temp = {}
			saveLeaf(node,_temp)
			result.append(_temp)
		else:
			searchLeaf(node.get_left(),result)
			searchLeaf(node.get_right(),result)
'''
将一颗树下的叶子结点聚到一起
返回的结果是
[{id:hash,id:hash},{id:hash,id:hash}]
'''		
def cluster(rootnode):
	result = []
	for root in rootnode:
		_temp = []
		searchLeaf(root,_temp)
		result.append(_temp)
	return result

