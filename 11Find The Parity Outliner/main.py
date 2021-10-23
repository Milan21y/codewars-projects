#https://www.codewars.com/kata/5526fc09a1bbd946250002dc/train/python

def find_outlier(integers):
    default = "None"
    aVen = integers[0]%2
    bVen = integers[1]%2
    cVen = integers[2]%2
    if aVen == 0 and bVen == 0:
        default = "0"
    elif aVen == 0 and cVen == 0:
        default = "0"
    elif bVen == 0 and cVen == 0:
        default = "0"
    else:
        default = "1"
    default = int(default)

    for element in integers:
        if element % 2 != default:
            return element

    
a = find_outlier([2, 16, 13])
print(a)