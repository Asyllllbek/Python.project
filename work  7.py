# price=int(input('цена товара: '))
# if price>9999:
#     sale = int(input('процент скидки: '))
#     price = price - ((price//100)*sale)
#     print('цена товара с учетом акции:',price)
# else:
#     print('скидка не доступна,цена товара:',price)

# order=int(input('цена товара: '))
# country=input('ваша страна: ')
# if (country=='USA' or  country=='Canada') and order>=10000:
#     print('Для вас доставка бесплатная')
# elif (country=='USA' or  country=='Canada') and order>=7000:
#     print('цена доставки : 10$')
# else:
#     print('цена доставки : 20$')

#numbers=[-3, 20, 0, -9, 100]
#result = 0
#for number in numbers:
#    if number>0:
#        result=result+number
#print(result)

#numbers=[100, 90, 80, 70, 60]
#user_int=int(input('введите число: '))
#result='число не найдено'
#for i in range(len(numbers)):
    #if numbers[i]==user_int:
        #result='число найдено'
#print(result)

# numbers=[1, 2, 2, 3, 4, 5, 2]
# new_number=[]
# for i in numbers:
#     if i not in new_number:
#         new_number.append(i)
# print(new_number)

# numbers=[-3,20, 0, -9, 100]
# for i in range(len(numbers)):
#     if numbers[i]<0:
#         numbers[i]=0
# print(numbers)

answer=['бумага']
mystery=('Чтоб читать и рисовать,')
my2=('Есть букварь и есть тетрадь. ')
my3=('Для нашего же блага ')
my4=('Придумана...')
print(mystery)
print(my2)
print(my3)
print(my4)
user_answer=(input("ваш ответ: "))
while user_answer not in answer:
    print('хорошенько подумайте и ответьте снова')
    user_answer = (input("ваш ответ: "))
if user_answer in answer:
    print('Правильно!!!')