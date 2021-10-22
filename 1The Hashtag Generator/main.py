#https://www.codewars.com/kata/52449b062fb80683ec000024/train/python
def generate_hashtag(s):
    if len(s.strip())+1 >= 140 or not s:
        return False
        
    else:
        words = s.split()
        words1 = []
        for element in words:
            words1.append(element.capitalize())
        result = "#" + "".join(words1)
    return result