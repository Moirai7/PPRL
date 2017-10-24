#-*- coding:utf-8 –*-
import pandas as pd

'''
组内求abs diff from \alpha(0.5)
'''
def generateRatios(group,alpha=0.5):
    _group = []
    for g in group:
	_temp = []
	for col in g.columns:
		try:
		    ratio = g[col].value_counts()[1]*1./len(g[col])
		except:
		    ratio = 0
		_temp.append(abs(ratio-alpha))
	_group.append(_temp)
    return _group

'''
求和
'''
def secureSummation(groups):
    _g = pd.DataFrame(groups)
    sums = _g.apply(sum)
    #return sums.idxmin()
    return sums

'''
选最佳
'''
def getBestBit(data):
    return data.idxmin()
