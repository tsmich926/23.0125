#작물과 가격이 함께 있는 리스트가 존재할때, 가장 높은 가격을 가지고 있는 작물의
#이름을 출력하라. 

grain_lst = [('고구마',3000), ('감자',2000), ('옥수수',4500),('토란',1300)]

# for i in grain_lst:
#     print(i)
#     for b in i:
#         print(b)

maxprice=0
for i in range(len(grain_lst)):
    print(i,grain_lst[i][1])
    if maxprice < grain_lst[i][1]:
        maxprice=grain_lst[i][1]
print(maxprice)
print(grain_lst[i][0])