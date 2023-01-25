#아스키코드
def caesar(word,n):
    res=''
    for w in word:
        if w.islower():
            divV=97
        else:
            divV=65

        dis=(ord(w) - divV + n) % 26 #a로부터 얼마나 떨어져있는지,몇바퀴 도는가
        res= res + chr(divV + dis)
    return res

print(caesar('apple',5))

"""""""""""""""""""""""""""""""""""""""""""
def is_position_safe(N,M,position):
    if M==0
    x-=1