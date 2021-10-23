#https://www.codewars.com/kata/59a96d71dbe3b06c0200009c/train/python

def generate_shape(integer):
    list1 = []
    blu = "\n"
    for i in range(0, integer):
        list1.append("+")
    var = "".join(list1)
    list2 = []
    for i in range(0, integer):
        if i == integer-1:
            list2.append(var)
        else:
            list2.append(var+blu)
    return("".join(list2))