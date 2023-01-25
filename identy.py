##주민등록번호를 입력받아 주민등록번호 뒤 
##7자리를 비식별화 하는 함수 de_identify를 만들어라


# input()
# def de_identify:
# s=input()
# p=list(s)
# for i in p(4:)
#     print(i)

# number=input()
# def de_identify(pnumber):
#     # number=input()
#     pnumber=list(number)
#     print(pnumber)
#     for i in range(6,14):
#         pnumber[i]='*'
#     return(pnumber)


# jumin=input()
# jumin=jumin.replace('-','')
# m=list(jumin[6:])
# lst=[]
# for i in range(len(m)):
#     m[i]='*'
#     lst=lst.append(m[i])
    # m[i]=m[i].replace('m[i]','*')
# print(m)
# print(m)
# app=''.join(m)
# print(app)

# 앞의 6글자 + *
# jumin=input()
# print(jumin)
# s=jumin[:6]
# m=s +'*******'
# print(m)

""""""""""""""""""""""""""""""""""""
def de_identify(jumin):
    jumin=jumin.replace('-','')
    m=list(jumin[6:])
    for i in range(len(m)):
        m[i]='*'
    m=''.join(m)
    return jumin[:6] + m



print(de_identify('000926-8789454'))