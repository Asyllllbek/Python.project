#counter=9
#while counter>0:
#    print(counter)
#    counter = counter -2

#password=['admin']
#user=input('введите пароль : ')
#while user not in password:
#    print('неверный пароль, попробуйте еще')
#    user=input('введите пароль : ')
#if user in password:
#    print('Правильно!!!')

#list = ["Java", "Python", "C++", "Pascal", "C#", "GoLang"]
#user_answer=(input("ваш ответ: "))
#while user_answer not in list:
#    print('хорошенько подумайте и ответьте снова')
#    user_answer = (input("ваш ответ: "))
#if user_answer in list:
#print('Правильно!!!')

print('1 пистолет')
print('2 РПГ')
print('3 нож')
print('0 выйти')
user=(int(input('выберите оружие: ')))
while user!=0:
    if user == 1:
        print('пиу пиу')
    elif user == 2:
        print('БДЫЩ')
    elif user == 3:
        print('ксинк')
    print('1 пистолет')
    print('2 РПГ')
    print('3 нож')
    print('0 выйти')
    user=(int(input('выберите оружие: ')))
print('вы вышли из игры')