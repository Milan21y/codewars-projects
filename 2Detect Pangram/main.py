#https://www.codewars.com/kata/545cedaa9943f7fe7b000048/train/python
def is_pangram(s):
    sList = []
    s = s.lower()
    sList[:0]=s
    print(sList)
    if "a" in sList and "b" in sList and "c" in sList and "d" in sList and "e" in sList and "f" in sList and "g" in sList and "h" in sList and "i" in sList and "j" in sList and "k" in sList and "l" in sList and "m" in sList and "n" in sList and "o" in sList and "p" in sList and "q" in sList and "r" in sList and "s" in sList and "t" in sList and "u" in sList and "v" in sList and "w" in sList and "x" in sList and "y" in sList and "z" in sList:
        return True
    else:
        return False

a = is_pangram("How quickly daft jumping zebras vex.")
print(a)