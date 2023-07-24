list = [7, -3, 9, -11, 18, 99, 2, 11]
# for i in range(0,3):
#     print(list[i],end=' ')
#
# for i in range(a-3,a):
#     print(list[i],end=' ')
a=len(list)
# for i in range(0,100):
#     if i==0:
#         print(i,end=' ')

# for i in range(0,a//2):
#     print(list[i])

# for i in range(a//2,a):
#     print(list[i])


# a = 0
# for i in range(len(list)):
#     if list[i]<a:
#         a = list[i]
# print(a)

# a = 0
# for i in range(len(list)):
#     if list[i]>a:
#         a = list[i]
# print(a)
list_2=[]
list_3=[]
# for i in range(1,len(list)-1):
#     print(list[i], end=' ')
for i in range(0,a):
    if list[i]<0:
        list_2.append(list[i])
print('отрицательных чисел: ',len(list_2))

for i in range(0,a):
    if list[i]>0:
        list_3.append(list[i])
print('положительных чисел: ',len(list_3))