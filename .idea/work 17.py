# dictionary = {
#     "a": 50,
#     "b": 20,
#     "c": 13.2,
#     "d": 70
# }
# word=dictionary.values()
# print(sum(word))
# key=(list(dictionary.keys()))
# counter=''
# for i in dictionary.keys():
#     counter=counter+i
# print(counter)


# friends = {
#     'Сергей': 'Павлодар',
#     'Айбек': 'Атырау',
#     'Дамир': 'Астана',
#     'Асылбек': 'Шымкент'
# }
# friends['Олжас']='Караганда'
#
# new_friends = {
#     'Амир': 'Алматы',
#     'Азат': 'Уральск',
#     'Руслан': 'Астана'
# }
# for i in new_friends:
#     friends[i]=new_friends[i]
# print(friends)
#
# friends.update(new_friends)
#print(friends)


# friends_names = ['Сергей', 'Айбек', 'Дамир', 'Рустем', 'Максим']
# friends_cities = ['Павлодар', 'Атырау', 'Астана', 'Алматы', 'Кокшетау']
#
# friends = {}
#
# for i in range(len(friends_names)):
#     name=friends_names[i]
#     city=friends_cities[i]
#     friends[name]=city
#
# print(friends)

#Домашняя Работа


# favorite_songs = {
#     'Сергей': ['Karma Police', 'Reptilia', 'No Surprises'],
#     'Дамир': ['Shake it out', 'The Show Must Go On', 'Наше лето'],
#     'Рустем': ['Владимирский централ', 'Той жыры', 'Аяулым']
# }
# print(len(favorite_songs['Дамир']))
# for i in favorite_songs['Рустем']:
#     print(i)



# playlist = {
#     'Venus As a Boy',
#     'Yesterday',
#     'Comfortably Numb',
#     'Time After Time',
# }
# new_music = [
#     'Stairway to Heaven',
#     'Wish You Were Here',
#     'Bohemian Rhapsody',
#     'Let It Be',
# ]
# for i in new_music:
#     if i not in playlist:
#         playlist.add(i)
# print(playlist, end='')


friends = {
    'Серёга': 'Павлодар',
    'Айбек': 'Атырау',
    'Дамир': 'Астана',
    'Рустем': 'Алматы',
    'Максим': 'Кокшетау'
}
def is_anyone_in(collection, city):
    for friend in collection:
        if collection[friend]==city:
            print('В городе', friends[friend], 'живёт', friend, '. Обязательно зайду в гости!')
        else:
            print('В городе', friends[friend], 'у меня есть друг, но мне туда не надо')
is_anyone_in(friends, 'Павлодар')