#https://www.codewars.com/kata/551dc350bf4e526099000ae5/train/python

def song_decoder(song):
    if "WUB" not in song:
        return song
    else:
        return " ".join(song.replace("WUB", " ").split())

"""
I didnt know how to finish this so i stole the code
"""