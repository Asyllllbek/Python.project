#
# def say_hello():
#     print('Привет, я Томирис!')
#     print('Я персональный помощник.')
#     print('Я ещё маленькая,')
#     print('но постоянно расту и умнею:')
#     print('ведь мой код каждый день дописывают!')
#
# say_hello()
# say_hello()


# def print_friends_count(friends_count):
#     if friends_count == 0:
#         print('У тебя нет друзей')
#     elif friends_count == 1:
#         print('У тебя', friends_count, 'друг')
#     elif friends_count >= 2 and friends_count <= 4:
#         print('У тебя', friends_count, 'друга')
#     elif friends_count >= 5 and friends_count < 20:
#         print('У тебя', friends_count, 'друзей')
#     else:
#         print('Ого, сколько у тебя друзей! Целых', friends_count)
#
# print_friends_count(0)
# print_friends_count(1)
# print_friends_count(2)
# print_friends_count(6)
# print_friends_count(20)


# def print_friends_count(friends_count):
#     if friends_count == 0:
#         print('У тебя нет друзей')
#     elif friends_count == 1:
#         print('У тебя', friends_count, 'друг')
#     elif friends_count >= 2 and friends_count <= 4:
#         print('У тебя', friends_count, 'друга')
#     elif friends_count >= 5 and friends_count < 20:
#         print('У тебя', friends_count, 'друзей')
#     else:
#         print('Ого, сколько у тебя друзей! Целых', friends_count)
#
# for i in range(0,21):
#     print_friends_count(i)



# def lets_go(name= 'Друг', target='учить Pyton'):
#     print(name + ', пойдём ' + target)
#
# lets_go()


# def lets_go(name= 'Друг', target='учить Pyton'):
#     print(name + ', пойдём ' + target)
#
# lets_go(target='читать следующий урок!')


#def multip(a,b):
#    print(a*b)
#
#a=int(input('первое число: '))
#b=int(input('виорое число: '))
#multip(a,b)

# def summa(list):
#     print(sum(list))
#
#
# numbers = [7,3,4,5,7]
#
# summa(numbers)
#
# numbers1 = [10,20,30,40]
# summa(numbers1)


def multip(a):
    for b in range(1, 11):
        print(a,'*',b,'=',a*b)
a=int(input('первое число: '))
multip(a)
