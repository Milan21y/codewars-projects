#https://www.codewars.com/kata/526571aae218b8ee490006f4/train/python

def count_bits(n):
    bits = f"{n:08b}"
    result = 0
    n = str(bits)
    print(n)
    nList = []
    nList[:0] = n
    if "1" in nList:
        print(nList)
        for element in nList:
            if element == "1":
                result = result+1
        return result
    else:
        return result
count_bits(0)