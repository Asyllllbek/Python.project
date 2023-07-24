#freak=['miki','salli','kevin']
#freak.append('jim')
#print(freak)

#que=int(input('Введите размер списпка: '))
#list=[]
#for i in range(1,que+1):
    #harry=int(input('Bведите число:'))
    #list.append(harry)
#print(list)
# 1 тап
#print((sum(list)))
# 2 тап
#max_number=max(list)
#print('Наибольшее число:',max_number)

# 3 тап
#numbers=[1,2,3,4,5,6,7,8,9,10]
#for number in reversed(numbers):
    #print(number,end=' ')

players_str=''

for i in reversed(range(1,11)):
    players_str=players_str+str(i)+', '
players_str=players_str+'кеттік'
print(players_str)