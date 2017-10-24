#-*- coding:utf-8 –*-


'''
分词
'''
def split(strWord = ""):
    if len(strWord) == 0:
        # error todo
        return
    splitList = []
    splitList.append("-"+strWord[0])
    splitList.append(strWord[-1]+"-")
    for i in range(len(strWord)-1):
        splitList.append(strWord[i:i+2])
    return splitList


def printList(strList = []):
    for i in range(len(strList)):
        print strList[i]



# list = split("hello")
# printList(list)
