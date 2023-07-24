# cities = [
#     'Алматы',
#     'Астана',
#     'Шымкент',
#     'Актобе',
#     'Караганда',
#     'Тараз',
#     'Павлодар',
#     'Семей',
#     'Астана',
#     'Кызылорда',
#     'Шымкент',
#     'Актау',
#     'Астана',
#     'Петропавловск',
#     'Алматы',
# ]
#
# unique_cities=set(cities)
# for i in unique_cities:
#     print('У меня есть друг в городе '+i)



# def print_valid_cities(barlyq_qalalar, oiynda_atalgan_qalalar):
#     oiynda_atalmagan_qalalar = barlyq_qalalar.difference(oiynda_atalgan_qalalar)
#     for i in oiynda_atalmagan_qalalar:
#         print(i)
all_cities = {
    'Алматы',
    'Астана',
    'Шымкент',
    'Актобе',
    'Караганда',
    'Тараз',
    'Павлодар',
    'Семей'
}
#
# used_cities = {'Алматы', 'Семей', 'Караганда'}
# print_valid_cities(all_cities, used_cities)

# def get_together_games(list_1, list_2):
# # Мұнда қиылыстарды табу үшін функция кодын жазыңыз
#     list_1 = set(list_1)
#     list_2 = set(list_2)
#     list_3 = list_1.intersection(list_2)
#     return list_3
# tomiris_games = [
#     'Online-chess',
#     'Города',
#     'DOOM',
#     'Крестики-нолики'
# ]
# alexa_games = [
#     'DOOM',
#     'Online-chess',
#     'Города',
#     'GTA',
#     'World of tanks'
# ]
# # Параметрлер ретінде ойын тізімдері бар функцияны шақырыңыз
# together_games =  (get_together_games(tomiris_games, alexa_games))
# # Циклдағы ойындардың тізімін басып шығарыңыз
# for i in together_games:
#     print('👾'+i)

# def print_valid_cities(all_cities, used_cities):
#     for city in all_cities.difference(used_cities):
#         print(city)
# def add_cities(all_cities, new_cities):
#     for city in new_cities:
#         all_cities.add(city)
# new_cities = [
#     'Атырау',
#     'Кызылорда',
#     'Костанай',
#     'Актау',
#     'Уральск',
#     'Петропавловск',
#     'Кокшетау',
# ]
# used_cities = {
#     'Алматы',
#     'Семей',
#     'Караганда'
# }
# add_cities(all_cities, new_cities)
# print_valid_cities(all_cities, used_cities)