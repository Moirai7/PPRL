#-*- coding:utf-8 –*-

import strCmp
import random
'''
判断两个block里的key是否有一个真正相等
'''
def checkReal(x,y,realSim):
	for s in realSim:
		for key1 in x:
			for key2 in y: 
				if (key1 in s) and (key2 in s):
					return True
	return False
'''
两个party相比较
'''
def compare(parties,realSim,alpha=0.7):
	party1 = parties[0]
	party2 = parties[1]
	times = 0
	real = 0
	checked1 = []
	checked2 = []
	merge = []
	for x in party1:
		for y in party2:
			if y.keys() not in checked2:
				key1 = random.choice(x.keys())
				key2 = random.choice(y.keys())
				times += 1
				precision = strCmp.strCmp(x[key1],y[key2])
				if precision>=alpha:
					print 'party m' + key1 + ' & party n' +key2 + '相似'
					if checkReal(x,y,realSim):
						print '上一行实际相似'
						real+=1
					merge.append(dict(x,**y))
					checked1.append(x.keys())
					checked2.append(y.keys())
					break
                                else:
					print 'party m' + key1 + ' & party n' +key2 + '不相似'
	for x in party1:
		if x.keys() not in checked1:
			merge.append(x)
	for y in party2:
		if y.keys() not in checked2:
			merge.append(y)
	return (merge,times,real)

def calParties(clusters):
        product = 1
        for c in clusters:
                _temp = 0
                for p in c:
                        _temp += len(p)
                if _temp != 0:
                        product *= _temp
        return product

def calSim(realSim):
	product = 0 
	for p in realSim:
		product += len(p)*(len(p)-1)/2
	return product

def printCluster(clusters):
        for c in clusters:
                for p in c:
                        for x in p:
                                print x,
                        print ' ',
                print ' '
'''
多个比较
第一实际应该计算多少次：m*n；实际有多少相似的求和C_n^2
'''
def compareAll(parties,realSim,alpha=0.7):
	times = 0
	real = 0
	n_times  = calParties(parties)
	n_real = calSim(realSim)
	print realSim
	while True:
		subid = random.sample(xrange(0,len(parties)),2)
		subid.sort(reverse=True)
		ids = []
		sub = []
		for x in subid:
			ids.append(x)
			sub.append(parties[x])
			del parties[x]
		print '-----------------------'
		printCluster(sub)
		merge,_times,_real = compare(sub,realSim,alpha)
		printCluster([merge])
		times += _times
		real += _real
		if len(parties)==0:
			break
		parties.append(merge)
	print 'times ratio: '+str(times*1.0/n_times)
	print 'precise ratio: '+str(real*1.0/n_real)
