# milk = True
# cereals = True
# eggs = not True
# if milk and cereals or eggs:
#     if eggs:
#         if milk:
#             breakfast = "- омлет"
#         else:
#             breakfast = "- яичница"
#     else:
#         breakfast = "- хлопья с молоком"
# else:
#     if milk:
#         breakfast = "- стакан молока"
#     elif cereals:
#         breakfast = "можно погрызть сухих хлопьев"
#     else:
#         breakfast = "ничего не будет: разгрузочный день"
# print("Сегодня на завтрак", breakfast)

# list=['windows','macos','ios','android', 'linux','rzbeuk']
# user_input=input('введите слово ')
# # if list[0]==user_input or list[1] == user_input or list[2] == user_input or list[3] == user_input:
# # g=len(list)
# # for i in range(g):
# #     if list[i]==user_input:
# #         print('слово найдено')
# if user_input in list:
#     print('слово найдено')
# else:
#     print('слово не найдено')

#temperature=int(input('temperatura: '))
#is_sunny=not True
#if temperature>26 and is_sunny:
    #print('жагажайга баруга болады')
#else:
    #print('uide bolgan durys')

age=int(input('Введите свой возраст: '))
if age<=12:
    print('детство')
elif age<=19:
    print('подростковый возраст')
elif age<=59:
    print('взрослая жизнь')
else:
    print('пенсионерский возраст')

# price=int(input('цена товара: '))
# if price>9999:
#     qwerty = price - (price / 10)
#     print('цена товара с учетом акции:',int(qwerty))
# else:
#     print('скидка не доступна,цена товара:',price)