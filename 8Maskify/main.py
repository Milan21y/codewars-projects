#https://www.codewars.com/kata/5412509bd436bd33920011bc/train/python

def maskify(cc):
    lenOfCC = len(cc)
    newLen = (lenOfCC-4)+1
    if lenOfCC == 0:
        return ""
    elif lenOfCC <= 4:
        return cc
    else:
        list1 = []
        list2 = []
        list1[:0] = cc
        list1.reverse()
        for i in range(0,4):
            a = list1[i]
            list2.append(a)
        list2.reverse()
        a = "".join(list2)
        outOfBlue = []
        for i in range(1, newLen):
            outOfBlue.append("#")
        return "".join(outOfBlue) + a