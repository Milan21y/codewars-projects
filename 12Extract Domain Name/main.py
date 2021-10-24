#https://www.codewars.com/kata/514a024011ea4fb54200004b/train/python

def domain_name(url):
    ands = 0
    if "https://www." in url:
        ands = 12
    elif "http://www." in url:
        ands = 11
    elif "https://" in url:
        ands = 8
    elif "http://" in url:
        ands = 7
    elif "www." in url:
        ands = 4
    res = ''
    for i in range(0, len(url)):
        if i>= ands:
            res = res + url[i]
    list2 = res.split(".")
    return list2[0]

print(domain_name("https://www.codewars.com"))