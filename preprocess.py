#-*- coding:utf-8 –*-

import pandas as pd
import random
import bloomFilter

'''
从csv读文件
安装pandas
'''
def readData(filename,col):
    data = pd.read_csv(filename, sep=',', header=0, index_col=False,dtype=str)[col]
    data[col] = data[col].astype(str)
    data['new'] = data.apply(lambda x:','.join(x),axis=1)
    return list(data['new'].values)

'''
corruption 
eg:
len(data)=10
分成3组
corruption是0.4

10/3=subsize(3) =》 3 3 4 
subsize(3)*0.4 =》1
subsize = (10-1)/3

subdata的格式是[['name11','name12','name13','repeat'],['name21','name22','name23','repeat']]
'''
def splitGroup(data,parties =3,corruption=0):
    subsize = len(data)/parties
    subdata = []
    _repeat = int(subsize * corruption)
    repeat = random.sample(data,_repeat)
    for x in repeat:
	data.remove(x)
    subsize = len(data)/parties
    for i in xrange(parties-1):
	    sub = random.sample(data,subsize)
	    for x in sub:
		#del data[data.index(x)]
	        data.remove(x)
	    if len(repeat)!=0:
		sub.extend(repeat)
	    subdata.append(sub)
    if len(repeat)!=0:
	    data.extend(repeat)
    subdata.append(data)
    return subdata,repeat

'''
暂时是n个实体中完全相同的记录作为相似
realSim的格式是[['id1','id2','id5'],['id3','id4','id6']]
表示的意思是'id1','id2','id5'相似，'id3','id4','id6'相似
TODO
'''
def calRealSim(data,repeat):
    realSim = []
    for x in repeat:
	#_sim = {}
	start = 0
	_sim = []
	for i in xrange(len(data)):
		#_sim[i]=str(start + data[i].index(x))
		_sim.append(str(start + data[i].index(x)))
		start+=len(data[i])
	realSim.append(_sim)
    return realSim

'''
算一下hash
parities的格式是[dataframe1,dataframe2]
dataframe里的列是 index,0,1,2,3.....999
'''
def hashGroup(_parties,hashnumber=100, length=1000):
    parities = []
    start = 0
    for p in _parties:
        _temp = []
        for m in p:
                _temp.append(bloomFilter.bf(m, hashnumber, length))
        parities.append(pd.DataFrame(_temp,index=xrange(start,start+len(_temp))))
	start += len(_temp)
    return parities
'''
取文件
分成不同group
实际相似的ids
hash
'''
def preprocess(filename='NO_DMV_Match.csv', col=['last_name','first_name','middle_name'], parties=3, corruption=0,hashnumber=100,length=1000):
    data = readData(filename,col)
    print 'read successfully!'
    _parities,repeat = splitGroup(data,parties,corruption)
    print 'split successfully!'
    realSim = calRealSim(_parities,repeat)
    print 'calSim successfully!'
    return hashGroup(_parities,hashnumber=100,length=1000),realSim
