# def literate(name,suren,age):
#     print('Аты:',name)
#     print('Тегі:',suren)
#     print('Жасы:',age)
# literate('Мағжан','Жұмабаев',45)


# def shof_date(day,mounth,year):
#     print('дата: ',day,'.',mounth,'.',year, sep='')
# shof_date(6,7,2023)


# def show_info(name,suren,age):
#     print('Аты:',name)
#     print('Тегі:',suren)
#     print('Жасы:',age)
# show_info('Сәкен','Сейфуллин',43)


# def multiply_sum(list):
#     counter=1
#     for i in list:
#         counter = counter*i
#     print(counter)
# numbers = [8,2,7,3,4]
# multiply_sum(numbers)

# def rooms_equal(room_size,room_list):
#     count=0
#     for room in room_list:
#         if room == room_size:
#             count = count + 1
#
#     print('Комнат площадью', room_size, 'кв.м:', count)
#
# flat = [5.55, 22.19, 7.78, 26.86, 5.55,29.84, 22.19, 5.55, 16.85, 4.52]
#
# hut = [9.2, 3.5, 8.1, 2.3, 9.2, 4.2, 6.9]
#
# rooms_equal(22.19, flat)
# rooms_equal(9.2,hut)

# phrase = 'Не волнуйтесь, если что-то не работает. Если бы всё работало, вас бы уволили.'
# def chitatt():
#     list=[]
#     for i in phrase:
#         if i=='Е' or i=='е':
#             list.append(i)
#     summa=len(list)
#     print(summa)
# chitatt()


# def number_of_occurrences(char, string):
#     count=0
#     for letter in string:
#         if letter==char:
#             count=count+1
#     print('Исходная строка:', string)
#     print('Количество вхождений символа', char, 'составляет:', count)
# phrase = 'Не волнуйтесь, если что-то не работает. Если бы всё работало, вас бы уволили.'
# number_of_occurrences('е', phrase)


# def count_vowels(string):
#     letters = 'aeiouy'
#     counter=0
#
#     for letter in string:
#         if letter in letters:
#             counter=counter+1
#
#     print(counter)
#
# text = input('текст: ')
# count_vowels(text)

def duble(first_name,second_name):

    third = []

    for i in first_name:
        if i in second_name and i not in third:
            third.append(i)

    return third

languages1 = ['java', 'python', 'c#', 'golang']
languages2 = ['php', 'javascript', 'java', 'python']
print(duble(languages1, languages2))