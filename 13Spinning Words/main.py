#This is a refactor! Original code was written 7 months ago!
#https://www.codewars.com/kata/5264d2b162488dc400000001/train/python/60a3dd2290321e00063e3f09

def spin_words(sentence):
    list1 = sentence.split()
    newList = []
    aList = []
    for element in list1:
        if len(element) >= 5:
            aList = []
            aList[:0] = element
            aList.reverse()
            a = "".join(aList)
            newList.append(a)
        else:
            newList.append(element)
    return " ".join(newList)


print (spin_words("This sentence is a sentence"))