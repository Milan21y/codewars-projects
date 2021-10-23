#https://www.codewars.com/kata/5502c9e7b3216ec63c0001aa/train/python
def open_or_senior(data):
    newList = []
    for element in data:
        first, second = element
        if first >= 55 and second >= 8:
            newList.append("Senior")
        else:
            newList.append("Open")
    return newList