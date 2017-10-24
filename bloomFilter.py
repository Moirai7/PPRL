#-*- coding:utf-8 –*-
import hashlib
import wordSplit

'''
@str            处理的字符串
@hashnumber     hash函数个数，默认20
@length         bloomfilter长度，默认1000
'''
def bf(str, hashnumber = 20, length = 1000):
    splitList = wordSplit.split(str)
    b = [0] * length

    for substr in splitList:
        # print "str = " + substr
        hash1 = hashlib.md5()
        hash1.update(substr)
        i_rnd1 = modOp(hash1.hexdigest(), length)
        b[i_rnd1] = 1
        # print i_rnd1

        hash2 = hashlib.sha1()
        hash2.update(substr)
        i_rnd2 = modOp(hash2.hexdigest(), length)
        b[i_rnd2] = 1
        # print i_rnd2

        #产生接下来的位数
        for i in range(1, hashnumber - 1):
            i_rnd = (i_rnd1 * i + i_rnd2) % length
            # print i_rnd
            b[i_rnd] = 1
    # print b
    return b




'''
对一个十六进制数取模操作
'''
def modOp(str = "", length = 1000):
    ret = 0
    for i in range(len(str)):
        ret = (ret * 16 + int(str[i], 16)) % length
    return ret



# src = 'th'
# print(bf(src, hashnumber=3, length=20))





