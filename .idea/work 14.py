# may_2022 = [26, 19, 13, 17, 20, 24, 12, 17, 21, 19, 20, 23, 26, 25, 24, 27, 26, 18, 20, 25, 31, 20, 22, 28, 30, 34, 31, 16, 27, 30, 24]
#
# # Осы функцияны толтырыңыз
# def comfort_count(temperatures):
#     count = 0
#     for temp in temperatures:
#         if 22 <= temp <= 26:
#             count += 1
#     # Функция, count айнымалысының мәнін қайтару керек
#     return count
# # Төмендегі кодты өзгертпеңіз:
# # comfort_count() функциясын шақырамыз, оған may_2022
# # тізімін береміз, жұмыс нәтижесін nice_days айнымалысына сақтаймыз
# nice_days = comfort_count(may_2022)
#
# # nice_days ішінде сақталған мәнді басып шығарамыз
# print('Количество тёплых дней в этом месяце:', nice_days)



# # Текшенің периметрін есептеу функциясы.
# def calc_cube_perimeter(side):
#     return side * 12
#
#
# # One_cube_perimeter айнымалысына calc_cube_perimeter()
# # функциясын 3 аргументімен қайтаратын мән беріңіз;
# # 3 метр - текше жиегінің ұзындығы.
# one_cube_perimeter =  calc_cube_perimeter(3)
#
# # 8 текше метрді салу үшін қажетті таяқтардың
# # жалпы ұзындығын есептеңіз және бұл мәнді
# # full_length айнымалысына сақтаңыз
# full_length = one_cube_perimeter*8
#
# # Енді нәтижені басып шығарыңыз (бұл жолда ештеңені өзгертудің қажеті жоқ)
# print('Необходимый метраж палок для 8 кубов:', full_length)



# # Текшенің ауданын есептеу функциясы.
# def calc_cube_area(side):
#     # Афанасий текшенің бір бетінің ауданын есептеу формуласын жазды:
#     one_face = side * side
#
#     # Текшенің толық ауданын есептеңіз: оның алты беті бірдей.
#     cube_area = one_face*6
#
#     # Үш нүктені алып тастаңыз және функцияны
#     # текшенің толық ауданын қайтаратындай етіп жазыңыз
#     return cube_area
# # One_cube_area айнымалысына қайтаратын мән беріңіз
# # calc_cube_area() функциясы 3 аргументімен;
# # 3 метр - текше жиегінің ұзындығы.
# one_cube_area = calc_cube_area(3)
#
# # 8 текшеге салу үшін қажет әйнектің жалпы
# # ауданын есептеңіз және бұл мәнді
# # full_area айнымалысына сақтаңыз
# full_area = one_cube_area*8
#
# print('Необходимая площадь стекла для 8 кубов, кв.м:', full_area)



# # Текшенің периметрін есептеу функциясы.
# def calc_cube_perimeter(side):
#     return side * 12
#
#
# # Текшенің ауданын есептеу функциясы.
# def calc_cube_area(side):
#     one_face = side * side
#     cube_area = one_face * 6
#     return cube_area
# # Функция туралы хабарландыруды толықтырыңыз:
# # енді екі параметрді қабылдау керек -
# # текше жиегінің ұзындығы және текшелер саны.
# def calc_cube(side, number_of_cubes):
#     one_cube_perimeter = calc_cube_perimeter(side)
#
#     # Мұнда үш нүктенің орнына екінші аргументте берілген
#     # текшелер санын сақтайтын айнымалы болуы керек.
#     full_length = one_cube_perimeter * number_of_cubes
#
#     one_cube_area = calc_cube_area(side)
#
#     # Мұнда үш нүктенің орнына екінші аргументте берілген
#     # текшелер санын сақтайтын айнымалы болуы керек.
#     full_area = one_cube_area * number_of_cubes
#
#     # Бұл жолда үш нүктелерді текшелер санын сақтайтын айнымалыға ауыстырыңыз
#     print('Для', number_of_cubes, 'кубов понадобится палок (м):', full_length, 'и стекла (кв.м):', int(full_area))
#
#
# # 3-текше жиегінің өлшемі,
# # 2-текшелердің қажетті саны
# calc_cube(2,4)
# calc_cube(0.5,26)
# calc_cube(0.61,6)



# def is_even(i):
#     return i % 2==0
#
#
# number=int(input('Ведите число: '))
# result=is_even(number)
# print(result)



# def average(numbers):
#     avera=sum(numbers)//len(numbers)
#     return avera
#
#
#
# list=[150,23,1,90,235]
# avg=average(list)
# print(avg)



# def reverse_string(text):
#     return text[::-1]
#
# def reversed_word():
#     for i in reversed(message):
#         print(i,end='')
#
# message=input('Введите фразу: ')
# reversed_word()
# reverse_string(message)

# def palindrome():
#     phrase = input("Введите фразу: ")
#
#     if phrase == phrase[::-1]:
#         print("True")
#     else:
#         print("False")
#
# palindrome()