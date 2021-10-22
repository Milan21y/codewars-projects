#https://www.codewars.com/kata/54da539698b8a2ad76000228/train/python

def is_valid_walk(walk):
    aString = "".join(walk)
    n = 0
    s = 0
    e = 0
    w = 0
    for element in walk:
        if element == "n":
            n = n+1
        elif element == "s":
            s = s+1
        elif element == "w":
            w = w+1
        elif element == "e":
            e = e+1
    if len(aString) == 10:
        if n - s == 0 and w - e == 0:
            return True
    else:
        return False
    return False
    