#-*- coding:utf-8 –*-



'''
比较两个字符串的相似度，采用的方法是jaccard
'''
def strCmp(bf1, bf2):
    if len(bf1) != len(bf2):
        return

    #统计都是1的个数
    countOne = 0
    countSame = 0
    for i in range(len(bf1)):
        if (bf1[i] + bf2[i] == 2):
            countOne += 1
            countSame += 1
        elif (bf1[i] + bf2[i] == 1):
            countOne += 1

    precision = 1.0 * countSame / countOne
    return precision
